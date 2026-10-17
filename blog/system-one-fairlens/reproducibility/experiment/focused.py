"""Five-question, all-image bilingual continuation from unchanged full-suite inputs."""
import argparse
from collections import Counter
from pathlib import Path
import time
import audit
import bilingual

SELECTED=('legal-07','legal-02','legal-04','legal-03','legal-09')

def prepare(data, previous, out):
    m=audit.load(data/'manifest.json')
    assert len(m['images'])==1505 and m['provenance']['task_identity_version']==2
    if not (data/'full-manifest.json').exists():
        audit.dump(data/'full-manifest.json',m)
    m['questions']=[q for q in m['questions'] if q['base_id'] in SELECTED]
    assert len(m['questions'])==10
    assert Counter(q['language'] for q in m['questions'])=={'en':5,'pt-BR':5}
    m['provenance'].update(focused_question_ids=list(SELECTED),expected_tasks=30100,
        replication_scope='Five selected original legal questions, all 1505 entries, both models and both languages',
        source_full_run=38918277052,selection_recorded_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        selection_note='Selected for the original criminality-bias objective after pilot and partial full-suite results existed. Analyses are exploratory. Original templates, options and task identities remain unchanged.')
    audit.dump(data/'manifest.json',m)
    imported=bilingual.seed(data,out,[previous])
    records=audit.latest_records(out.glob('predictions-*.jsonl'))
    pending={}
    for model in audit.MODELS:
        tasks=audit.tasks(m,[model],0,1,1)
        pending[model]=sum(records.get(t[0],{}).get('status') not in ('ok','unscored_response') for t in tasks)
    summary={**imported,'expected_tasks':30100,'pending_by_model':pending,'primary_question':'legal-07',
             'question_ids':list(SELECTED),'selection_note':m['provenance']['selection_note']}
    audit.dump(out/'focused-coverage.json',summary)
    return summary

if __name__=='__main__':
    import json
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data',type=Path,default=audit.ROOT/'data')
    p.add_argument('--previous',type=Path,required=True)
    p.add_argument('--out',type=Path,default=audit.ROOT/'results')
    a=p.parse_args()
    print(json.dumps(prepare(a.data,a.previous,a.out),indent=2))
