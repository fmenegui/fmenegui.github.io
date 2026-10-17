"""Check the complete blog CSV against saved inputs, outputs and final counts."""
import argparse
from collections import Counter, defaultdict
import csv
import gzip
import hashlib
import json
from pathlib import Path
import sys


def verify(bundle):
    csv.field_size_limit(32*1024*1024)
    sys.path.insert(0,str(bundle/'reproducibility/experiment'))
    sys.path.insert(0,str(bundle/'reproducibility/experiment/publication'))
    from audit_release import audit, validate
    # The same reconstruction routine is included in the bundle.
    sys.path.insert(0,str(bundle/'reproducibility'))
    from export_blog_csv import request_template, score_column
    checks=json.loads((bundle/'checksums.json').read_text())
    for name,digest in checks.items():
        assert hashlib.sha256((bundle/name).read_bytes()).hexdigest()==digest,name
    manifest=json.loads((bundle/'reproducibility/metadata/manifest.json').read_text())
    images={r['id']:r for r in manifest['images']}
    questions={q['id']:q for q in manifest['questions']}
    planned={t[0] for t in audit.tasks(manifest,list(audit.MODELS),0,1,1)}
    schema=json.loads((bundle/'data/csv-schema.json').read_text())
    counts=Counter();totals=defaultdict(Counter);seen=set();pairs=defaultdict(set)
    with gzip.open(bundle/'data/fairlens-responses.csv.gz','rt',encoding='utf-8',newline='') as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==schema['columns']
        last_pair=None;last_model=None
        for row in reader:
            record=json.loads(row['record_json'])
            image=images[row['image_id']];q=questions[row['question_id']]
            check=validate(record,image,q)
            task=row['task_id']
            assert task==record['task_id'] and task in planned and task not in seen
            seen.add(task)
            assert row['input_image_sha256']==image['png_sha256']
            assert row['source_image_sha256']==image['source_sha256']
            assert row['source_filename']==image['filename']
            assert row['prompt']==q['prompt'] and row['prompt_sha256']==audit.digest(q['prompt'].encode())
            assert row['language']==q['language'] and row['domain']==q['domain']
            for field in ('model','requested_model','served_model','status'):
                assert row[field]==record[field]
            assert json.loads(row['api_response_json'])==record['raw_response']
            assert json.loads(row['api_answer_json'])==record['answer']
            assert json.loads(row['api_usage_json'])==record.get('usage')
            assert json.loads(row['api_call_json'])==request_template(record['model'],q,image['png_sha256'],record['requested_model'])
            assert json.loads(row['options_json'])==q['choices']
            assert json.loads(row['to_canonical_json'])==q['to_canonical']
            expected=q['to_canonical'][q['expected']]
            choice=q['to_canonical'].get(record.get('choice'))
            assert row['benchmark_expected_answer']==expected
            assert row['predicted_answer']==(choice or '')
            assert int(row['explicit_refusal'])==check['refusal']
            assert int(row['soundness_match'])==(choice==expected)
            cp={q['to_canonical'][k]:v for k,v in record['probabilities'].items()} if not check['refusal'] else None
            assert json.loads(row['canonical_probabilities_json'])==cp
            for col,option in schema['probability_columns'].items():
                if cp is None or option not in cp:assert row[col]==''
                else:assert float(row[col])==cp[option]
            key=(row['model'],row['language'],row['domain'])
            totals[key]['total']+=1
            totals[key]['correct']+=int(row['soundness_match'])
            totals[key]['refusal']+=int(row['explicit_refusal'])
            counts[(row['model'],row['language'])]+=1
            pair=(row['image_id'],row['base_question_id'],row['language'])
            pairs[pair].add(row['model'])
            if pair==last_pair:
                assert last_model=='jev' and row['model']=='gpt-decisions'
            else:assert row['model']=='jev'
            last_pair,last_model=pair,row['model']
    assert seen==planned and len(seen)==schema['rows']==228760
    assert len(pairs)==114380 and all(p==set(audit.MODELS) for p in pairs.values())
    assert set(counts.values())=={57190}
    original=json.loads((bundle/'reproducibility/metadata/audit-summary.json').read_text())
    for prior in original['domain_counts']:
        assert totals[(prior['model'],prior['language'],prior['domain'])]=={k:prior[k] for k in ('total','correct','refusal')}
    return {'verified_rows':len(seen),'paired_model_groups':len(pairs),'columns':len(schema['columns']),
            'all_api_responses_match_saved_records':True,'all_reconstructed_requests_verified':True,
            'all_probability_columns_verified':True,'file_checksums_verified':len(checks)}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--bundle',type=Path,required=True)
    a=p.parse_args();print(json.dumps(verify(a.bundle.resolve()),indent=2))
