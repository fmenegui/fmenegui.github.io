"""Run the unmodified, checksum-verified FairLens closed-question metric programs."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.request
import audit

FILES={
 'config/load.py':'473cd0eb19417d1d781958a0303546576eef15d9',
 'config/questions.json':'0cc51fa9c04e4a48890eff05aa4ada3e3bdffbf7',
 'eval/statistical/evaluate_soundness.py':'d371a635d69709b21c80d13e93dbde32373da6cc',
 'eval/statistical/evaluate_demographic_parity.py':'e7ec12fb999c31383e04c8ae669a4fa6ea61d1ef',
 'eval/statistical/evaluate_demographic_associations.py':'6871411d403232fec3671e581f0defd6249c41c7',
}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,default=audit.ROOT/'results')
    a=p.parse_args()
    root=audit.ROOT/'.upstream/src/fairlens'
    provenance={}
    for filename,expected in FILES.items():
        url=f'https://raw.githubusercontent.com/vectorinstitute/fairlens/{audit.UPSTREAM}/src/fairlens/{filename}'
        with urllib.request.urlopen(url,timeout=45) as r:
            raw=r.read()
        actual=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual!=expected:
            raise ValueError('Pinned upstream file checksum mismatch: '+filename)
        path=root/filename
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(raw)
        provenance[filename]={'url':url,'git_blob_sha':actual,'sha256':audit.digest(raw)}
    for model in audit.MODELS:
        for language in ('en','pt-BR'):
            for domain in ('hiring','legal','healthcare'):
                input_file=a.out/'upstream-format'/model/language/(domain+'_results.json')
                for metric in ('soundness','demographic_parity','demographic_associations'):
                    script=root/'eval/statistical'/('evaluate_'+metric+'.py')
                    run=subprocess.run([sys.executable,str(script),str(input_file),'--domain',domain,'--json'],
                                       check=True,capture_output=True,text=True,timeout=120)
                    audit.dump(a.out/'upstream-metrics'/model/language/(domain+'-'+metric+'.json'),json.loads(run.stdout))
    audit.dump(a.out/'upstream-metrics/provenance.json',{'upstream_commit':audit.UPSTREAM,'files':provenance,
       'options':'PT responses map bijectively to the original English labels before evaluation',
       'missing_http':'Omitted from upstream input, never imputed. Coverage is in metrics-bilingual.json.',
       'refusals':'Kept as UNPARSED_REFUSAL. Original upstream programs include these in denominators.',
       'free_text':'Unavailable for target endpoints, no judge metric computed.'})
    print('Wrote all 36 original closed-question metric reports')

if __name__=='__main__':
    main()
