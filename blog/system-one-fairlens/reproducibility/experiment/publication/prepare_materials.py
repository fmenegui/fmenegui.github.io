"""Assemble figures, source, full tables and pending human review materials."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]


def load(p): return json.loads(p.read_text())


def prepare(package, results):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                         'svg.fonttype':'none','savefig.dpi':210})
    package.mkdir(parents=True,exist_ok=True)
    for name in ('figures','manuscript','translation-review','metrics','code/publication','code/tests','upstream/fairlens'):
        (package/name).mkdir(parents=True,exist_ok=True)
    summary=load(package/'data/audit-summary.json')
    manifest=load(package/'data/manifest.json')
    metrics=load(results/'metrics-bilingual.json')
    groups=load(results/'groups-summary.json')
    for name in ('metrics-bilingual.json','groups-summary.json','groups-summary.md'):
        shutil.copy2(results/name,package/'metrics'/name)
    shutil.copytree(results/'artifact/results/upstream-metrics',package/'metrics/upstream-metrics',dirs_exist_ok=True)
    shutil.copytree(ROOT/'.upstream/src/fairlens',package/'upstream/fairlens',dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    for p in ROOT.glob('*.py'): shutil.copy2(p,package/'code'/p.name)
    for pattern in ('*.py','*.md','*.bib','requirements-document.txt'):
        for p in (ROOT/'publication').glob(pattern): shutil.copy2(p,package/'code/publication'/p.name)
    for p in (ROOT/'tests').glob('test_*.py'): shutil.copy2(p,package/'code/tests'/p.name)
    for name in ('requirements.txt','questions.en.original.json','translations.pt-BR.json','bilingual-launch.json',
                 'PROTOCOL-BILINGUAL.md','GROUPED-PROTOCOL.md','README.md'):
        shutil.copy2(ROOT/name,package/'code'/name)
    shutil.copy2(ROOT/'publication/manuscript.md',package/'manuscript/manuscript.md')
    shutil.copy2(ROOT/'publication/references.bib',package/'manuscript/references.bib')
    shutil.copy2(ROOT/'publication/review-notes.pt-BR.md',package/'review-notes.pt-BR.md')
    (package/'README.md').write_bytes((ROOT/'publication/README.md').read_bytes())
    (package/'THIRD_PARTY.md').write_text('''# Third party source provenance

The FairLens question configuration, config loader and three statistical metric programs in upstream/fairlens are unchanged from VectorInstitute/fairlens commit 130205f243267fc90b973cb875d1711c2d932bbe. Per file Git blob and SHA256 checksums are in metrics/upstream-metrics/provenance.json. Cite Khazaie, Radwan and Raza, arXiv:2609.01691 (2026).

The pinned repository tree has no separate LICENSE file. Its README identifies UTKFace as noncommercial research data. No new license or redistribution permission is conferred by this author review package. Dataset access, attribution and applicable source rights remain with their respective holders and must be resolved before public distribution. No face image bytes are included.
''')
    review=['# Independent translation review packet','',
            'Status: pending. No independent human translation review has been performed.', '',
            'Record reviewer name, qualifications and date. Translate PT back into English before comparing with the source when practical. Evaluate meaning, scenario assumptions, option equivalence, gender marking, register and expected label interpretation. Keep model outcomes hidden during the semantic review when practical. Every changed wording must be a new version. Do not overwrite executed prompts.', '',
            'The companion review.csv has one row per source question, plus context and suffix rows. Fields start pending or empty. A pass is a human judgment, not a structural option check.', '']
    translation=load(ROOT/'translations.pt-BR.json')
    original=load(ROOT/'questions.en.original.json')
    rows=[]
    def add(qid,kind,en,pt,options=''):
        rows.append(dict(id=qid,kind=kind,english=en,portuguese=pt,option_mapping=options,
                         human_status='pending',reviewer='',review_date='',back_translation='',
                         meaning_equivalent='',context_assumptions_equivalent='',options_equivalent='',
                         grammatical_gender_notes='',proposed_revision='',adjudication=''))
        review.extend(['## '+qid,'','Type: '+kind,'','English','',en,'','Português','',pt,''])
        if options: review.extend(['Option mapping','',options,''])
    for domain in ('hiring','legal','healthcare'):
        add('context-'+domain,'context',original['system_prompts'][domain],translation['system_prompts'][domain])
    add('suffix-closed','suffix','Please select one of the provided options and output only that option.',translation['closed_suffix'])
    add('suffix-open','suffix','Answer the question as best as you can.',translation['open_suffix'])
    english=[q for q in manifest['inventory'] if q['language']=='en']
    for q in english:
        pt=translation['questions'][q['base_id']]
        add(q['base_id'],q['type']+(' executed' if q['type']=='closed' else ' not executed'),q['text'],pt['text'],
            json.dumps(pt.get('option_map',{}),ensure_ascii=False) if q['type']=='closed' else '')
    assert len(rows)==74
    (package/'translation-review/review-packet.md').write_text('\n'.join(review)+'\n')
    with (package/'translation-review/review.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    # All question outcomes and every test are included, not just highlighted findings.
    fields=['model','language','question_id','expected','total','categories','refusals','correct','soundness_all',
            'soundness_categories','choices']
    with (package/'metrics/all-question-outcomes.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for model, qs in metrics['questions'].items():
            for qid,v in qs.items():
                q=next(q for q in manifest['questions'] if q['id']==qid)
                v=v['overall'];correct=round(v['soundness']*v['scored']) if v['scored'] else 0
                w.writerow(dict(model=model,language=q['language'],question_id=qid,expected=q['to_canonical'][q['expected']],
                                total=v['attempted'],categories=v['scored'],refusals=v['explicit_refusals'],correct=correct,
                                soundness_all=correct/v['attempted'],soundness_categories=v['soundness'],choices=json.dumps(v['choices'],ensure_ascii=False)))
    tests=[dict(model=model,question_id=qid,**t) for model,qs in metrics['language_comparison'].items() for qid,v in qs.items() for t in v['tests']]
    assert len(tests)==260
    (package/'metrics/all-paired-tests.json').write_text(json.dumps(tests,indent=2)+'\n')
    with (package/'metrics/refusal-demographics.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(summary['refusal_demographics'][0]));w.writeheader();w.writerows(summary['refusal_demographics'])
    domain_rows=[]
    for r in summary['domain_counts']:
        model,lang,domain=(r[k] for k in ('model','language','domain'))
        base=package/'metrics/upstream-metrics'/model/lang
        dp=load(base/(domain+'-demographic_parity.json'))
        da=load(base/(domain+'-demographic_associations.json'))
        groups_da=[v for v in da['overall']['race'].values() if isinstance(v,dict) and 'total' in v]
        nn=sum(v['choices']['non_neutral'] for v in groups_da)
        den=sum(v['total'] for v in groups_da)
        row={**r,'soundness_all':r['correct']/r['total'],'category_coverage':(r['total']-r['refusal'])/r['total'],
             'association_nonneutral_original_count':nn,'association_original_denominator':den,
             'association_original_unparsed':sum(v['unparsed'] for v in groups_da),
             'association_rate_original':nn/den,
             'association_rate_categories':metrics['domain_summary'][model][lang][domain]['association_non_neutral_rate']}
        for attr in ('race','gender','age'):
            row['parity_gap_original_'+attr]=dp['overall'][attr]['max_gap']
            row['association_gap_original_'+attr]=da['overall'][attr]['non_neutral_max_gap']
        domain_rows.append(row)
    with (package/'metrics/all-domain-summary.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(domain_rows[0]));w.writeheader();w.writerows(domain_rows)
    # Figure 1 uses independently reconstructed integer counts.
    conditions=[('jev','en','Jev EN'),('jev','pt-BR','Jev PT'),('gpt-decisions','en','GPT EN'),('gpt-decisions','pt-BR','GPT PT')]
    fig,axes=plt.subplots(1,3,figsize=(10.2,3.15),sharex=True,sharey=True)
    for ax,domain,title in zip(axes,('hiring','legal','healthcare'),('Hiring','Legal','Healthcare')):
        data=[next(r for r in summary['domain_counts'] if (r['model'],r['language'],r['domain'])==(m,l,domain)) for m,l,_ in conditions]
        correct=np.array([r['correct']/r['total']*100 for r in data])
        refused=np.array([r['refusal']/r['total']*100 for r in data])
        wrong=100-correct-refused
        y=np.arange(4)
        ax.barh(y,correct,color='#277C8E',height=.57,label='Expected category')
        ax.barh(y,wrong,left=correct,color='#D8A45D',height=.57,label='Other category')
        ax.barh(y,refused,left=correct+wrong,color='#A9AFB7',height=.57,label='Explicit refusal')
        ax.set_title(title,fontsize=11,pad=9)
        ax.set_xlim(0,100);ax.set_xticks([0,50,100]);ax.set_xlabel('Assigned tasks (%)')
        ax.set_yticks(y,[c[2] for c in conditions]);ax.tick_params(axis='y',length=0)
        ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
    axes[0].invert_yaxis()
    handles,labels=axes[0].get_legend_handles_labels();fig.legend(handles,labels,loc='lower center',ncol=3,frameon=False,bbox_to_anchor=(.52,-.04))
    fig.tight_layout(rect=(0,.07,1,1))
    for ext in ('png','svg'): fig.savefig(package/'figures'/('domain-outcomes.'+ext),bbox_inches='tight')
    plt.close(fig)
    # Figure 2 keeps a common fixed 0–100 scale across all groups.
    names=['Interview invitations','Post interview shortlist','Qualifications and roles','Hiring trust','Clinical judgments','Healthcare roles','Healthcare trust','Legal judgments']
    matrix=[]
    for group in groups['groups'].values():
        row=[]
        for m,l,_ in conditions:
            v=group['models'][m]['languages'][l]
            row.append(round(v['soundness_scored']*v['scored'])/v['terminal']*100)
        matrix.append(row)
    matrix=np.array(matrix)
    fig,ax=plt.subplots(figsize=(8.8,3.55))
    im=ax.imshow(matrix,cmap='YlGnBu',vmin=0,vmax=100,aspect='auto')
    ax.set_xticks(range(4),[c[2] for c in conditions]);ax.set_yticks(range(8),names)
    ax.tick_params(length=0);ax.xaxis.tick_top()
    for y in range(8):
        for x in range(4): ax.text(x,y,f'{matrix[y,x]:.2f}',ha='center',va='center',color='white' if matrix[y,x]>=65 else '#15212C',fontsize=10)
    for spine in ax.spines.values():spine.set_visible(False)
    cb=fig.colorbar(im,ax=ax,fraction=.035,pad=.03);cb.set_label('Soundness (%)');cb.set_ticks([0,50,100])
    fig.tight_layout()
    for ext in ('png','svg'): fig.savefig(package/'figures'/('group-soundness.'+ext),bbox_inches='tight')
    plt.close(fig)
    print(json.dumps({'review_rows':len(rows),'closed_question_variants':76,'outcome_rows':152,'paired_tests':len(tests),'figures':2}))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package',type=Path,required=True);p.add_argument('--results',type=Path,required=True)
    a=p.parse_args();prepare(a.package,a.results)
