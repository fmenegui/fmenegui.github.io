"""Continue every FairLens closed question and publish coverage-aware group reports."""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import time
import audit
import bilingual

GROUPS={
 'hiring-interview':('Convites para entrevista',[f'hiring-{i:02d}' for i in range(1,7)]),
 'hiring-shortlist':('Seleção após entrevista',[f'hiring-{i:02d}' for i in range(7,13)]),
 'hiring-profile':('Qualificações, liderança e ocupação',[f'hiring-{i:02d}' for i in range(13,19)]),
 'hiring-trust':('Confiança e competência profissional',[f'hiring-{i:02d}' for i in range(19,22)]),
 'healthcare-clinical':('Saúde, urgência e dor',[f'healthcare-{i:02d}' for i in range(1,5)]),
 'healthcare-roles':('Funções na área da saúde',['healthcare-05','healthcare-06']),
 'healthcare-trust':('Confiança e competência médica',['healthcare-07','healthcare-08']),
 'legal':('Segurança e criminalidade',[f'legal-{i:02d}' for i in range(1,10)]),
}
TERMINAL={'ok','unscored_response'}

def validate_groups(manifest):
    listed=[q for _,ids in GROUPS.values() for q in ids]
    source={q['base_id'] for q in manifest['questions']}
    assert len(listed)==len(set(listed))==38 and set(listed)==source
    assert len(manifest['questions'])==76


def question_group(data,target,group):
    m=audit.load(data/'manifest.json')
    validate_groups(m)
    title,ids=GROUPS[group]
    m['questions']=[q for q in m['questions'] if q['base_id'] in ids]
    m['provenance'].update(focused_question_ids=ids,expected_tasks=1505*len(ids)*4,
        question_group=group,question_group_title=title,
        replication_scope=f'All official entries, {len(ids)} original closed questions in {group}, both models and languages',
        interim_inference_note='Exploratory interim estimates. Group analyses do not replace the final global multiplicity correction. No inference about actual criminality, health or competence.')
    target.mkdir(parents=True,exist_ok=True)
    audit.dump(target/'manifest.json',m)
    link=target/'images'
    if not link.exists():
        link.symlink_to((data/'images').resolve(),target_is_directory=True)
    return m


def count_rows(rows,qmap):
    states=Counter(r['status'] for r in rows)
    ok=[r for r in rows if r['status']=='ok']
    refusals=sum(r.get('answer',{}).get('type')=='refusal' for r in rows)
    return {'recorded':len(rows),'terminal':sum(states[s] for s in TERMINAL),
        'scored':len(ok),'refusals':refusals,'unrecognized':states['unscored_response']-refusals,
        'http_errors':states['http_error'],'states':dict(states),
        'soundness_scored':audit.mean([float(r['choice']==qmap[r['question_id']]['expected']) for r in ok]),
        'adverse_rate_scored':audit.mean([float(r['choice']==qmap[r['question_id']]['adverse']) for r in ok if qmap[r['question_id']].get('adverse')])}


def snapshot(data,out,folders=None):
    m=audit.load(data/'manifest.json')
    validate_groups(m)
    folders=folders or [out]
    records=audit.latest_records([p for folder in folders for p in folder.rglob('predictions-*.jsonl')])
    qm={q['id']:q for q in m['questions']}
    by_question=defaultdict(list)
    states=Counter()
    for task_id,image,q,model,_,_ in audit.tasks(m,list(audit.MODELS),0,1,1):
        if task_id not in records:
            states['missing']+=1
            continue
        r=records[task_id]
        assert r['image_id']==image['id'] and r['png_sha256']==image['png_sha256']
        assert r['prompt_sha256']==audit.digest(q['prompt'].encode())
        states[r['status']]+=1
        by_question[(model,q['id'])].append(r)
    result={'expected_tasks':228760,'states':dict(states),'terminal_tasks':sum(states[s] for s in TERMINAL),
        'recorded_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'groups':{},
        'interpretation':'Partial-group estimates describe available responses only. HTTP failures and missing tasks are not No or Cannot tell. Refusals are separate. No causal conclusions from demographic gaps.',
        'full_metrics_file':'metrics-bilingual.json'}
    for group,(title,ids) in GROUPS.items():
        g={'title':title,'question_ids':ids,'expected_tasks':1505*len(ids)*4,'models':{}}
        for model in audit.MODELS:
            rows=[r for q in m['questions'] if q['base_id'] in ids for r in by_question[(model,q['id'])]]
            summary=count_rows(rows,qm)
            summary['expected_tasks']=1505*len(ids)*2
            summary['coverage']=summary['terminal']/summary['expected_tasks']
            summary['languages']={lang:count_rows([r for q in m['questions'] if q['base_id'] in ids and q['language']==lang for r in by_question[(model,q['id'])]],qm) for lang in bilingual.LANGUAGES}
            pairs=[]
            for qid in ids:
                en={r['image_id']:r for r in by_question[(model,qid)]}
                pt={r['image_id']:r for r in by_question[(model,qid+'-pt-BR')]}
                pairs.extend((en[i],pt[i]) for i in sorted(en.keys()&pt.keys()))
            summary['paired_terminal_n']=sum(a['status'] in TERMINAL and b['status'] in TERMINAL for a,b in pairs)
            valid=[(a,b) for a,b in pairs if a['status']=='ok' and b['status']=='ok']
            summary['paired_scored_n']=len(valid)
            differences=[]
            for a,b in valid:
                q=qm[a['question_id']]
                pq=qm[b['question_id']]
                differences.append(float(b['choice']==pq['expected'])-float(a['choice']==q['expected']))
            summary['paired_soundness_change_pt_minus_en']=audit.mean(differences)
            g['models'][model]=summary
        g['complete']=all(v['terminal']==v['expected_tasks'] for v in g['models'].values())
        result['groups'][group]=g
    audit.dump(out/'groups-summary.json',result)
    lines=['# FairLens: acompanhamento por grupo','',
        f"Respostas terminais: {result['terminal_tasks']:,} de 228.760. Incluem escolhas válidas e recusas.",'',
        'Estimativas parciais sobre respostas disponíveis. A composição pode mudar com a conclusão das pendências.','',
        '| Grupo | Perguntas | Jev concluído | GPT concluído |','|---|---:|---:|---:|']
    for g in result['groups'].values():
        lines.append(f"| {g['title']} | {len(g['question_ids'])} | {100*g['models']['jev']['coverage']:.1f}% | {100*g['models']['gpt-decisions']['coverage']:.1f}% |")
    lines += ['','Soundness corresponde à resposta esperada pelos autores, não à acurácia sobre atributos reais das pessoas. Recusas não são a opção de abstenção.','',
              '| Grupo e modelo | EN soundness nas respostas classificáveis | PT soundness nas respostas classificáveis | Recusas EN / PT | Pares classificáveis |','|---|---:|---:|---:|---:|']
    fmt=lambda v:f'{100*v:.1f}%' if v is not None else 'NA'
    for g in result['groups'].values():
        for model,s in g['models'].items():
            en,pt=s['languages']['en'],s['languages']['pt-BR']
            lines.append(f"| {g['title']} / {model} | {fmt(en['soundness_scored'])} (n={en['scored']}) | {fmt(pt['soundness_scored'])} (n={pt['scored']}) | {en['refusals']} / {pt['refusals']} | {s['paired_scored_n']} |")
    lines += ['','As taxas marginais EN/PT podem usar conjuntos diferentes quando há pendências ou recusas. A mudança pareada e seus denominadores estão em groups-summary.json. Inferência por pergunta, intervalos e testes pareados estão em metrics-bilingual.json.','A seleção anterior de cinco perguntas serviu para priorizar a retomada e não exclui perguntas do conjunto final de 38. As 31 abertas continuam sem suporte nos dois endpoints.']
    (out/'groups-summary.md').write_text('\n'.join(lines)+'\n')
    return {'terminal_tasks':result['terminal_tasks'],'states':dict(states),'groups':len(GROUPS)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=('group','snapshot','run'))
    p.add_argument('--data',type=Path,default=audit.ROOT/'data')
    p.add_argument('--out',type=Path,default=audit.ROOT/'results')
    p.add_argument('--group',choices=tuple(GROUPS))
    p.add_argument('--previous',type=Path,nargs='*')
    p.add_argument('--model',choices=tuple(audit.MODELS))
    p.add_argument('--min-interval',type=float,default=0.5)
    a=p.parse_args()
    if a.command=='group':
        target=a.data.parent/'group-data'
        m=question_group(a.data,target,a.group)
        result=bilingual.seed(target,a.out,a.previous)
        result.update(group=a.group,questions_per_language=len(m['questions'])//2)
    elif a.command=='snapshot':
        result=snapshot(a.data,a.out,a.previous)
    else:
        plan=audit.run(a.data,a.out,[a.model],0,1,1,0,True)
        if plan['pending']:
            result=audit.run(a.data,a.out,[a.model],0,1,1,plan['pending'],False,a.min_interval)
        else:
            result=plan
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
