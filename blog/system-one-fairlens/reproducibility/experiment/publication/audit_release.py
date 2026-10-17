"""Offline audit and lossless consolidation of the completed FairLens artifact.

No inference, credentials or network access. See README.md for the release contract.
"""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import sqlite3
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import audit
import bilingual


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), sort_keys=True)


def validate(record, image, question):
    """Fail closed on metadata, task identity and any normalization discrepancy."""
    assert record['png_sha256'] == image['png_sha256'], 'PNG checksum mismatch'
    assert record['prompt_sha256'] == audit.digest(question['prompt'].encode()), 'Prompt mismatch'
    for key in ('race', 'gender', 'age'):
        assert int(record[key]) == int(image[key]), 'Demographic metadata mismatch'
    for key in ('language', 'domain'):
        # Seed records predate explicit language/domain fields. Their v2 task,
        # question ID and prompt hash bind the same metadata unambiguously.
        assert record.get(key, question[key]) == question[key], f'{key} mismatch'
    assert record['expected'] == question['expected']
    assert record.get('adverse') == question.get('adverse'), 'Adverse label mismatch'
    assert record['repeat'] == 0
    assert record['requested_model'] == audit.MODELS[record['model']][1]
    assert record['task_id'] == audit.task_key(image, question, record['model'], record['requested_model'], 0, 2)
    normalized = audit.normalize(record['model'], record['raw_response'], question)
    for key in normalized:
        assert normalized[key] == record.get(key), f'Normalizer discrepancy: {key}'
    served = 'jev-1.14.0' if record['model'] == 'jev' else 'gpt-6-luna'
    assert record['served_model'] == served, 'Unexpected served version'
    refusal = normalized['answer'].get('type') == 'refusal'
    if record['status'] == 'unscored_response':
        assert refusal, 'Unknown unscored response'
        return {'refusal': True}
    assert record['status'] == 'ok' and not refusal
    assert normalized['answer'].get('type') == 'choice'
    assert normalized['probabilities_valid'], 'Invalid probability vector'
    probabilities = normalized['probabilities']
    # A score tie is allowed. Retain the returned decision, do not recompute it.
    deficit = max(probabilities.values()) - probabilities[normalized['choice']]
    return {'refusal': False, 'sum_error': abs(sum(probabilities.values()) - 1),
            'argmax_deficit': deficit,
            'tie': sum(abs(p - max(probabilities.values())) < 1e-12 for p in probabilities.values()) > 1}


def consolidate(source, out):
    out.mkdir(parents=True, exist_ok=True)
    dbpath = out / 'audit-working.sqlite'
    for suffix in ('', '-journal', '-wal', '-shm'):
        dbpath.with_name(dbpath.name+suffix).unlink(missing_ok=True)
    db = sqlite3.connect(dbpath)
    # Scratch database is fully reproducible. Avoid enormous rollback journals.
    db.execute('pragma journal_mode=off')
    db.execute('create table records(task text primary key, status text, body text, source text)')
    states = Counter()
    conflicting_terminal = set()
    with zipfile.ZipFile(source) as archive:
        manifest = json.loads(archive.read('data/manifest.json'))
        images = {r['id']: r for r in manifest['images']}
        questions = {q['id']: q for q in manifest['questions']}
        planned = {r[0] for r in audit.tasks(manifest, list(audit.MODELS), 0, 1, 1)}
        assert len(planned) == 228760
        for path in sorted(n for n in archive.namelist() if Path(n).name.startswith('predictions-') and n.endswith('.jsonl')):
            for line in archive.open(path):
                r = json.loads(line)
                states[r['status']] += 1
                if r['task_id'] not in planned:
                    continue
                old = db.execute('select status,body from records where task=?', (r['task_id'],)).fetchone()
                if old and old[0] != 'http_error' and r['status'] != 'http_error':
                    prior = json.loads(old[1])
                    if prior.get('raw_response') != r.get('raw_response'):
                        conflicting_terminal.add(r['task_id'])
                if old is None or old[0] == 'http_error' or r['status'] != 'http_error':
                    db.execute('insert or replace into records values (?,?,?,?)', (r['task_id'], r['status'], encode(r), path))
            db.commit()
            print('Consolidated', path, flush=True)
    assert db.execute('select count(*) from records').fetchone()[0] == len(planned)
    assert not conflicting_terminal, 'Conflicting terminal responses require manual investigation'
    summary = Counter()
    grouped = defaultdict(Counter)
    question_counts = defaultdict(Counter)
    refusal_demographics = defaultdict(Counter)
    max_error = defaultdict(float)
    max_deficit = defaultdict(float)
    ties = Counter()
    reconstructed_metadata = Counter()
    sum_mismatches = Counter()
    argmax_examples = []
    schema = ['task_id','image_id','png_sha256','model','served_model','language','question_id','base_id',
              'domain','race','gender','age','status','explicit_refusal','choice','expected','adverse',
              'sound','cannot_tell','adverse_selected','adverse_score','probabilities_valid']
    with (out/'responses.jsonl').open('w') as raw, (out/'observations.csv').open('w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=schema)
        writer.writeheader()
        for task, body in db.execute('select task,body from records order by task'):
            r = json.loads(body)
            q, image = questions[r['question_id']], images[r['image_id']]
            check = validate(r, image, q)
            for field in ('language', 'domain'):
                if field not in r:
                    reconstructed_metadata[field] += 1
            # Preserve raw records losslessly. Derive CSV columns from manifest.
            language, domain = q['language'], q['domain']
            summary[r['status']] += 1
            key = (r['model'], language, domain)
            counts = grouped[key]
            counts['total'] += 1
            qc = question_counts[(r['model'],language,q['base_id'])]
            qc['total'] += 1
            refusal = check['refusal']
            if not refusal:
                max_error[r['model']] = max(max_error[r['model']], check['sum_error'])
                max_deficit[r['model']] = max(max_deficit[r['model']], check['argmax_deficit'])
                ties[r['model']] += check['tie']
                sum_mismatches[r['model']] += check['sum_error'] > 1e-9
                if check['argmax_deficit'] > 1e-9:
                    argmax_examples.append({k:r[k] for k in ('task_id','model','image_id','question_id','choice','probabilities')})
            choice = q['to_canonical'].get(r.get('choice'))
            expected = q['to_canonical'][q['expected']]
            adverse = q['to_canonical'].get(q.get('adverse'))
            correct = choice == expected
            counts['correct'] += correct
            counts['refusal'] += refusal
            qc['correct'] += correct
            qc['refusal'] += refusal
            qc['choice:'+str(choice)] += not refusal
            for attr, label in bilingual.attributes(r).items():
                rc = refusal_demographics[(r['model'],language,domain,attr,label)]
                rc['total'] += 1
                rc['refusal'] += refusal
                rc['correct'] += correct
            p = r.get('probabilities',{})
            writer.writerow({**{k:r[k] for k in ('task_id','image_id','png_sha256','model','served_model','question_id','race','gender','age','status')},
                'language':language, 'domain':domain,
                'base_id':q['base_id'], 'explicit_refusal':int(refusal), 'choice':choice or '', 'expected':expected,
                'adverse':adverse or '', 'sound':int(correct), 'cannot_tell':int(choice=='Cannot tell'),
                'adverse_selected':int(choice==adverse) if adverse else '',
                'adverse_score':p[q['adverse']] if adverse and not refusal else '',
                'probabilities_valid':int(r.get('probabilities_valid',False))})
            raw.write(encode(r)+'\n')
    # Cross-check the independently reconstructed counts against the final analyzer.
    original = json.loads((source.parent/'metrics-bilingual.json').read_text())
    for (model,language,domain), counts in grouped.items():
        prior = original['domain_summary'][model][language][domain]
        assert counts['total'] == prior['recorded']
        assert counts['correct'] == round(prior['soundness']*prior['scored'])
        assert counts['refusal'] == prior['recorded']-prior['scored']
    assert summary == {'ok':211999, 'unscored_response':16761}
    result = {'schema_version':1, 'expected_tasks':len(planned), 'terminal_counts':dict(summary),
        'source_archive_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'checkpoint_line_states_including_duplicates':dict(states),
        'conflicting_terminal_tasks':len(conflicting_terminal),
        'normalization_matches_raw_response':True, 'metadata_and_task_hashes_verified':True,
        'legacy_metadata_derived_in_csv':dict(reconstructed_metadata),
        'valid_vectors':211999, 'max_probability_sum_error':dict(max_error),
        'max_selected_choice_argmax_deficit':dict(max_deficit), 'argmax_ties':dict(ties),
        'probability_sum_mismatch_count':dict(sum_mismatches),
        'selected_choice_not_displayed_argmax_count':len(argmax_examples),
        'selected_choice_not_displayed_argmax_examples':argmax_examples,
        'domain_counts':[dict(model=k[0],language=k[1],domain=k[2],**v) for k,v in sorted(grouped.items())],
        'question_counts':[dict(model=k[0],language=k[1],question=k[2],**v) for k,v in sorted(question_counts.items())],
        'refusal_demographics':[dict(model=k[0],language=k[1],domain=k[2],attribute=k[3],group=k[4],**v)
                                for k,v in sorted(refusal_demographics.items())]}
    (out/'audit-summary.json').write_text(json.dumps(result, indent=2)+'\n')
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    templates = []
    for q in manifest['questions']:
        for model, (_, model_id) in audit.MODELS.items():
            url, body = audit.payload(model,b'IMAGE_BYTES_PLACEHOLDER',q,model_id)
            if model == 'jev':
                body['assets']['audit-image']['data_base64'] = '<BASE64_PNG_MATCHING_MANIFEST_SHA256>'
            else:
                body['input'][0]['content'][1]['image_url'] = 'data:image/png;base64,<BASE64_PNG_MATCHING_MANIFEST_SHA256>'
            templates.append({'model':model,'question_id':q['id'],'endpoint':url,'body':body,
                'non_secret_headers':{'Content-Type':'application/json',**({'TypeSafe-Danger-Zone-Images':'true'} if model=='jev' else {})}})
    (out/'request-templates.json').write_text(json.dumps({'note':'Reconstructed from executed adapter and manifest. Original wire request bodies were not separately logged. No authorization headers or image bytes included.', 'templates':templates}, ensure_ascii=False,indent=2)+'\n')
    db.close()
    dbpath.unlink()
    print(json.dumps({k:v for k,v in result.items() if k not in ('domain_counts','question_counts','refusal_demographics')},indent=2))
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--artifact',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    consolidate(a.artifact,a.out)


if __name__=='__main__':
    main()
