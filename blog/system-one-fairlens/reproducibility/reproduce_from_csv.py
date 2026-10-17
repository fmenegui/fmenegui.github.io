"""Rebuild every statistical result from the blog CSV, without inference."""
import argparse
import csv
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def reproduce(bundle,out):
    from verify_blog_csv import verify
    for key in ('JEV_MODEL','GPT_DECISIONS_MODEL'):
        if os.getenv(key):raise ValueError('Unset '+key+' for reproducibility')
    verified=verify(bundle)
    sys.path.insert(0,str(bundle/'reproducibility/experiment'))
    sys.path.insert(0,str(bundle/'reproducibility/experiment/publication'))
    import audit,bilingual
    from verify_release import assert_equivalent
    out.mkdir(parents=True,exist_ok=True)
    target=out/'predictions-from-csv.jsonl'
    with target.open('w') as dest,gzip.open(bundle/'data/fairlens-responses.csv.gz','rt',encoding='utf-8',newline='') as f:
        for row in csv.DictReader(f):
            dest.write(row['record_json']+'\n')
    bilingual.analyze(bundle/'reproducibility/metadata',out)
    original=bundle/'reproducibility/metrics'
    actual=json.loads((out/'metrics-bilingual.json').read_text())
    assert_equivalent(actual,json.loads((original/'metrics-bilingual.json').read_text()))
    upstream=bundle/'reproducibility/upstream/fairlens'
    provenance=json.loads((original/'upstream-metrics/provenance.json').read_text())
    for relative,meta in provenance['files'].items():
        raw=(upstream/relative).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==meta['git_blob_sha']
    reports=0
    for model in audit.MODELS:
        for lang in ('en','pt-BR'):
            for domain in ('hiring','legal','healthcare'):
                for metric in ('soundness','demographic_parity','demographic_associations'):
                    result=subprocess.run([sys.executable,str(upstream/'eval/statistical'/('evaluate_'+metric+'.py')),
                        str(out/'upstream-format'/model/lang/(domain+'_results.json')),'--domain',domain,'--json'],
                        capture_output=True,text=True,check=True)
                    expected=json.loads((original/'upstream-metrics'/model/lang/(domain+'-'+metric+'.json')).read_text())
                    regenerated=json.loads(result.stdout);assert_equivalent(regenerated,expected)
                    p=out/'upstream-metrics'/model/lang/(domain+'-'+metric+'.json')
                    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(regenerated,indent=2)+'\n')
                    reports+=1
    return {**verified,'bilingual_statistics_reproduced':True,'original_metric_reports_reproduced':reports,
            'paid_inference_calls':0,'float_relative_tolerance':1e-12,'float_absolute_tolerance':1e-300}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bundle',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();print(json.dumps(reproduce(a.bundle.resolve(),a.out.resolve()),indent=2))
