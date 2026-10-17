"""Verify the exported release offline, optionally regenerating all analyses."""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_release import audit, bilingual, validate


def assert_equivalent(actual, expected, path='metrics'):
    """Exact structure/counts, relative 1e-12 tolerance for numerical libraries."""
    if isinstance(actual,float) and isinstance(expected,float):
        assert math.isclose(actual,expected,rel_tol=1e-12,abs_tol=1e-300), path
    elif isinstance(actual,dict) and isinstance(expected,dict):
        assert actual.keys()==expected.keys(), path
        for key in actual: assert_equivalent(actual[key],expected[key],path+'/'+key)
    elif isinstance(actual,list) and isinstance(expected,list):
        assert len(actual)==len(expected), path
        for i,(a,b) in enumerate(zip(actual,expected)): assert_equivalent(a,b,path+'/'+str(i))
    else:
        assert type(actual)==type(expected) and actual==expected, path


def verify(package, full_out=None):
    from scipy.stats import binomtest
    for name in ('JEV_MODEL','GPT_DECISIONS_MODEL'):
        if os.environ.get(name):
            raise ValueError('Unset model overrides for offline reproducibility: '+name)
    checks=json.loads((package/'checksums.json').read_text())
    for relative, expected in checks.items():
        assert hashlib.sha256((package/relative).read_bytes()).hexdigest()==expected, relative
    m=json.loads((package/'data/manifest.json').read_text())
    inv=bilingual.inventory(package/'upstream/fairlens/config')
    assert inv==m['inventory']
    assert [q for q in inv if q['type']=='closed']==m['questions']
    images={r['id']:r for r in m['images']}
    questions={q['id']:q for q in m['questions']}
    expected={t[0] for t in audit.tasks(m,list(audit.MODELS),0,1,1)}
    seen=set()
    counts=defaultdict(Counter)
    probability_checks=defaultdict(Counter)
    paired=defaultdict(dict)
    for line in (package/'data/responses.jsonl').open():
        r=json.loads(line)
        assert r['task_id'] in expected and r['task_id'] not in seen
        seen.add(r['task_id'])
        q=questions[r['question_id']]
        checked=validate(r,images[r['image_id']],q)
        if not checked['refusal']:
            pc=probability_checks[r['model']]
            pc['sum_mismatch']+=checked['sum_error']>1e-9
            pc['choice_not_argmax']+=checked['argmax_deficit']>1e-9
            pc['beyond_two_decimals']+=any(abs(p*100-round(p*100))>1e-9 for p in r['probabilities'].values())
        key=(r['model'],q['language'],q['domain'])
        c=counts[key]
        c['total']+=1
        c['correct']+=r.get('choice')==q['expected']
        c['refusal']+=r['answer'].get('type')=='refusal'
        paired[(r['model'],q['base_id'],q['language'])][r['image_id']]={
            'choice':q['to_canonical'].get(r.get('choice')), 'png':r['png_sha256'],
            'ok':r['status']=='ok', 'refusal':r['answer'].get('type')=='refusal'}
    assert seen==expected
    summary=json.loads((package/'data/audit-summary.json').read_text())
    for model,pc in probability_checks.items():
        assert pc['sum_mismatch']==summary['probability_sum_mismatch_count'][model]
        assert pc['beyond_two_decimals']==0
    assert sum(pc['choice_not_argmax'] for pc in probability_checks.values())==summary['selected_choice_not_displayed_argmax_count']
    for row in summary['domain_counts']:
        assert dict(counts[(row['model'],row['language'],row['domain'])])=={k:row[k] for k in ('total','correct','refusal')}
    report=json.loads((package/'metrics/metrics-bilingual.json').read_text())
    tests=[]
    ambiguous=set(m['ambiguous_demographic_hashes'])
    for model, comparisons in report['language_comparison'].items():
        for qid, comparison in comparisons.items():
            q=questions[qid]
            expected_label=q['to_canonical'][q['expected']]
            adverse=q['to_canonical'].get(q.get('adverse'))
            en,pt=(paired[(model,qid,lang)] for lang in ('en','pt-BR'))
            for prior in comparison['tests']:
                endpoint=prior['endpoint']
                representative=[]
                hashes=set()
                for image_id in sorted(en.keys() & pt.keys()):
                    a,b=en[image_id],pt[image_id]
                    if endpoint!='refusal' and not (a['ok'] and b['ok']):
                        continue
                    if a['png'] in ambiguous or a['png'] in hashes:
                        continue
                    hashes.add(a['png'])
                    representative.append(image_id)
                def indicator(row):
                    if endpoint=='refusal': return row['refusal']
                    if endpoint=='soundness': return row['choice']==expected_label
                    if endpoint=='abstention': return row['choice']=='Cannot tell'
                    if endpoint=='adverse': return row['choice']==adverse
                    raise ValueError(endpoint)
                up=sum(not indicator(en[i]) and indicator(pt[i]) for i in representative)
                down=sum(indicator(en[i]) and not indicator(pt[i]) for i in representative)
                assert prior['n']==len(representative)
                assert prior['en0_pt1']==up and prior['en1_pt0']==down
                p=float(binomtest(up,up+down).pvalue) if up+down else 1.0
                assert math.isclose(prior['p_value'],p,rel_tol=1e-12,abs_tol=1e-300)
                if representative:
                    assert math.isclose(prior['estimate'],(up-down)/len(representative),abs_tol=1e-14)
                else:
                    assert prior['estimate'] is None
                tests.append({'p_value':p,'saved_holm':prior['p_holm']})
    bilingual.holm(tests)
    assert len(tests)==260
    assert all(math.isclose(t['p_holm'],t['saved_holm'],rel_tol=1e-12,abs_tol=1e-300) for t in tests)
    with (package/'data/observations.csv').open() as f:
        assert sum(1 for _ in csv.DictReader(f))==len(expected)
    if full_out:
        full_out.mkdir(parents=True,exist_ok=True)
        checkpoint=full_out/'predictions-release.jsonl'
        if checkpoint.exists() or checkpoint.is_symlink(): checkpoint.unlink()
        checkpoint.symlink_to((package/'data/responses.jsonl').resolve())
        bilingual.analyze(package/'data',full_out)
        regenerated=json.loads((full_out/'metrics-bilingual.json').read_text())
        assert_equivalent(regenerated,report)
        provenance=json.loads((package/'metrics/upstream-metrics/provenance.json').read_text())
        for relative,meta in provenance['files'].items():
            raw=(package/'upstream/fairlens'/relative).read_bytes()
            blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
            assert blob==meta['git_blob_sha']
        for model in audit.MODELS:
            for lang in ('en','pt-BR'):
                for domain in ('hiring','legal','healthcare'):
                    for metric in ('soundness','demographic_parity','demographic_associations'):
                        result=subprocess.run([sys.executable,str(package/'upstream/fairlens/eval/statistical'/('evaluate_'+metric+'.py')),
                            str(full_out/'upstream-format'/model/lang/(domain+'_results.json')),'--domain',domain,'--json'],
                            check=True,capture_output=True,text=True)
                        saved=json.loads((package/'metrics/upstream-metrics'/model/lang/(domain+'-'+metric+'.json')).read_text())
                        assert_equivalent(json.loads(result.stdout),saved)
        checkpoint.unlink()
    return {'verified_tasks':len(seen),'verified_paired_tests':len(tests),
            'package_files_verified':len(checks),'full_regeneration':bool(full_out),
            'probability_checks':{k:dict(v) for k,v in probability_checks.items()}}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package',type=Path,required=True)
    p.add_argument('--full-out',type=Path)
    args=p.parse_args()
    print(json.dumps(verify(args.package,args.full_out),indent=2))
