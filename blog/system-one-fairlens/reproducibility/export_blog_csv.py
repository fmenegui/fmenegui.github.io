"""Export one complete, auditable CSV row per image/question/language/model.

Offline only. Raw response bodies and saved records are preserved. Request
bodies are reconstructed from the executed adapter, with a hash-bound image
placeholder replacing image bytes. No credentials or images are exported.
"""
import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import sqlite3
import sys

ROOT=Path(__file__).resolve().parents[1]
if (Path(__file__).resolve().parent/'experiment/audit.py').exists():
    ROOT=Path(__file__).resolve().parent/'experiment'
sys.path.insert(0,str(ROOT))
import audit
sys.path.insert(0,str(ROOT/'publication'))
from audit_release import validate

DATASET='https://huggingface.co/datasets/vector-institute/fairlens'
PAPER='https://arxiv.org/abs/2609.01691'


def compact(v):
    return json.dumps(v,ensure_ascii=False,separators=(',',':'),sort_keys=True)


def score_column(option):
    return 'probability_'+re.sub(r'[^a-z0-9]+','_',option.lower()).strip('_')


def request_template(model, question, image_hash, requested):
    url,body=audit.payload(model,b'',question,requested)
    placeholder='<BASE64_PNG_SHA256:'+image_hash+'>'
    if model=='jev':
        body['assets']['audit-image']['data_base64']=placeholder
    else:
        body['input'][0]['content'][1]['image_url']='data:image/png;base64,'+placeholder
    return {'method':'POST','url':url,'headers':{'Content-Type':'application/json',
            **({'TypeSafe-Danger-Zone-Images':'true'} if model=='jev' else {})},'body':body}


def export(package, out):
    out.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((package/'data/manifest.json').read_text())
    images={r['id']:r for r in manifest['images']}
    questions={q['id']:q for q in manifest['questions']}
    options=sorted({o for q in questions.values() for o in q['canonical_options']})
    assert len({score_column(o) for o in options})==len(options)
    by_hash=defaultdict(list)
    for image in images.values():by_hash[image['png_sha256']].append(image['id'])
    ambiguous=set(manifest['ambiguous_demographic_hashes'])
    columns=['task_id','image_id','source_filename','source_image_sha256','input_image_sha256',
        'source_width','source_height','input_width','input_height','padding_left','padding_top','padding_rgb_json',
        'model','requested_model','served_model','language','domain','question_id','base_question_id','question_format',
        'prompt','prompt_sha256','options_json','canonical_options_json','to_canonical_json',
        'benchmark_expected_answer','benchmark_expected_answer_local','benchmark_adverse_answer','benchmark_adverse_answer_local',
        'api_endpoint','api_method','api_call_json','request_reconstructed','authorization_environment_variable',
        'api_response_json','api_answer_json','api_usage_json','record_json','status','explicit_refusal',
        'predicted_answer','predicted_answer_local','cannot_tell','soundness_match','adverse_selected',
        'probabilities_json','canonical_probabilities_json','probabilities_valid','probability_sum','selected_is_displayed_argmax',
        'latency_s','response_time_utc','time_ns','repeat','source_task_id',
        'race_annotation','race_label','gender_annotation','gender_label','age_annotation','age_group',
        'duplicate_png','demographic_annotation_conflict','first_official_id_for_png','eligible_unique_input',
        'dataset_url','article_url','benchmark_source_commit','source_mirror_url']+[score_column(o) for o in options]
    dbpath=out.parent/'blog-export-working.sqlite'
    for suffix in ('','-journal','-wal','-shm'):dbpath.with_name(dbpath.name+suffix).unlink(missing_ok=True)
    db=sqlite3.connect(dbpath)
    db.execute('pragma journal_mode=off')
    db.execute('create table r(task text primary key,image text,q text,lang text,model_order integer,body text)')
    for i,line in enumerate((package/'data/responses.jsonl').open(),1):
        r=json.loads(line);q=questions[r['question_id']]
        db.execute('insert into r values(?,?,?,?,?,?)',(r['task_id'],r['image_id'],q['base_id'],q['language'],0 if r['model']=='jev' else 1,line))
        if i%10000==0:db.commit()
    db.commit()
    counts=Counter()
    totals=defaultdict(Counter)
    first_image=manifest['images'][0]['id']
    examples=[]
    path=out/'fairlens-responses.csv.gz'
    with path.open('wb') as raw, gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0,compresslevel=9) as gz:
        text=io.TextIOWrapper(gz,encoding='utf-8',newline='')
        writer=csv.DictWriter(text,fieldnames=columns,lineterminator='\n')
        writer.writeheader()
        for i,(body,) in enumerate(db.execute('select body from r order by image,q,lang,model_order'),1):
            r=json.loads(body);image=images[r['image_id']];q=questions[r['question_id']]
            checked=validate(r,image,q)
            refusal=checked['refusal']
            choice=q['to_canonical'].get(r.get('choice'))
            probs=r.get('probabilities') if not refusal else None
            cp={q['to_canonical'][k]:v for k,v in probs.items()} if probs is not None else None
            expected=q['to_canonical'][q['expected']]
            adverse=q['to_canonical'].get(q.get('adverse'))
            call=request_template(r['model'],q,image['png_sha256'],r['requested_model'])
            sha=image['png_sha256']
            first=min(by_hash[sha])
            row={'task_id':r['task_id'],'image_id':image['id'],'source_filename':image['filename'],
                'source_image_sha256':image['source_sha256'],'input_image_sha256':sha,
                'source_width':image['source_size'][0],'source_height':image['source_size'][1],
                'input_width':image['size'][0],'input_height':image['size'][1],
                'padding_left':image['padding_left_top'][0],'padding_top':image['padding_left_top'][1],'padding_rgb_json':'[128,128,128]',
                'model':r['model'],'requested_model':r['requested_model'],'served_model':r['served_model'],
                'language':q['language'],'domain':q['domain'],'question_id':q['id'],'base_question_id':q['base_id'],
                'question_format':'binary' if len(q['choices'])==2 else 'multiple_choice',
                'prompt':q['prompt'],'prompt_sha256':r['prompt_sha256'],'options_json':compact(q['choices']),
                'canonical_options_json':compact(q['canonical_options']),'to_canonical_json':compact(q['to_canonical']),
                'benchmark_expected_answer':expected,'benchmark_expected_answer_local':q['expected'],
                'benchmark_adverse_answer':adverse or '', 'benchmark_adverse_answer_local':q.get('adverse') or '',
                'api_endpoint':call['url'],'api_method':'POST','api_call_json':compact(call),'request_reconstructed':1,
                'authorization_environment_variable':'JEV_API_KEY' if r['model']=='jev' else 'OPENAI_API_KEY',
                'api_response_json':compact(r['raw_response']),'api_answer_json':compact(r['answer']),
                'api_usage_json':compact(r.get('usage')),'record_json':compact(r),'status':r['status'],
                'explicit_refusal':int(refusal),'predicted_answer':choice or '', 'predicted_answer_local':r.get('choice') or '',
                'cannot_tell':int(choice=='Cannot tell'),'soundness_match':int(choice==expected),
                'adverse_selected':int(choice==adverse) if adverse and not refusal else '',
                'probabilities_json':compact(probs),'canonical_probabilities_json':compact(cp),
                'probabilities_valid':int(r.get('probabilities_valid',False)),
                'probability_sum':sum(probs.values()) if probs is not None else '',
                'selected_is_displayed_argmax':int(checked['argmax_deficit']<1e-9) if not refusal else '',
                'latency_s':r.get('latency_s',''),
                'response_time_utc':datetime.fromtimestamp(r['time_ns']/1e9,tz=timezone.utc).isoformat(),
                'time_ns':r['time_ns'],'repeat':r['repeat'],'source_task_id':r.get('source_task_id',''),
                'race_annotation':image['race'],'race_label':audit.RACES[int(image['race'])],
                'gender_annotation':image['gender'],'gender_label':{0:'Male',1:'Female'}[int(image['gender'])],
                'age_annotation':image['age'],'age_group':'young' if image['age']<30 else 'middle' if image['age']<60 else 'senior',
                'duplicate_png':int(len(by_hash[sha])>1),'demographic_annotation_conflict':int(sha in ambiguous),
                'first_official_id_for_png':first,'eligible_unique_input':int(sha not in ambiguous and image['id']==first),
                'dataset_url':DATASET,'article_url':PAPER,'benchmark_source_commit':manifest['provenance']['upstream_commit'],
                'source_mirror_url':manifest['provenance']['image_acquisition']['url'],
                **{score_column(o):cp[o] if cp is not None and o in cp else '' for o in options}}
            writer.writerow(row)
            counts[(r['model'],q['language'])]+=1
            c=totals[(r['model'],q['language'],q['domain'])]
            c['total']+=1;c['correct']+=row['soundness_match'];c['refusal']+=refusal
            if image['id']==first_image and q['id']=='legal-07':examples.append(row)
            if i%50000==0:print('Exported rows',i,flush=True)
        text.flush()
    assert sum(counts.values())==228760
    summary=json.loads((package/'data/audit-summary.json').read_text())
    for prior in summary['domain_counts']:
        assert totals[(prior['model'],prior['language'],prior['domain'])]=={k:prior[k] for k in ('total','correct','refusal')}
    with (out/'example-two-models.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=columns,lineterminator='\n');w.writeheader();w.writerows(examples)
    (out/'examples.json').write_text(json.dumps({'selection':'First official manifest entry, legal-07 in English, both models. Not selected by outcome.','rows':examples},ensure_ascii=False,indent=2)+'\n')
    descriptions={
        'api_call_json':'Reconstructed method, endpoint, non-secret headers and original adapter body. Image bytes replaced with a SHA256-bound placeholder. Not an original wire log.',
        'api_response_json':'Complete saved API response body, including served model and usage where returned. HTTP response headers were not recorded.',
        'record_json':'Complete saved terminal record. Retains legacy task migration metadata and raw response. Parse to reconstruct the original response JSONL.',
        'benchmark_expected_answer':'Logical FairLens target for this question, in canonical English. This is not a verified real-world attribute of the pictured person.',
        'input_image_sha256':'SHA256 of exact padded PNG sent to both APIs.',
        'source_image_sha256':'SHA256 of acquired cropped source image before RGB conversion and padding.',
        'race_label':'Original dataset annotation for grouping, not a model prediction or self-identified demographic fact.',
        'eligible_unique_input':'Global first official ID for a nonconflicting unique PNG. Paired/category analyses select first eligible pairs separately, so use the provided analysis code.',
        'probability_sum':'Sum as returned, without renormalization.',
        'selected_is_displayed_argmax':'Whether returned category matches a maximum displayed score, accepting ties. Null for refusals.',
        'adverse_selected':'1 for benchmark adverse category, 0 for other supplied categories, null for refusal or no adverse target.',
        'soundness_match':'1 for expected category, 0 otherwise including an explicit refusal. Keeps every terminal task in the benchmark denominator.',
        'request_reconstructed':'Always 1. Requests reconstructed from executed code and manifest. Authentication secrets and image bytes are excluded.'}
    schema={'format':'UTF-8 RFC4180-style CSV with comma delimiter and JSON-escaped fields, gzip compressed',
        'rows':228760,'columns':columns,'probability_columns':{score_column(o):o for o in options},'descriptions':descriptions,
        'missing':'Empty scalar or score cells denote not applicable or unavailable, never an imputed zero. JSON fields use null when no vector exists.',
        'order':'image_id, base question ID, language, model with Jev followed by GPT',
        'row_unit':'One official image entry × closed question × language × model',
        'credentials':'None included. The environment variable name identifies the credential to supply for a separately authorized future call.',
        'api_call_note':'Base64 placeholder is replaced with the locally reconstructed image whose hash matches input_image_sha256. Future hosted outputs may differ.',
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size,
        'counts':[{'model':m,'language':l,'rows':n} for (m,l),n in sorted(counts.items())]}
    (out/'csv-schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')
    db.close();dbpath.unlink()
    print(json.dumps({k:schema[k] for k in ('rows','bytes','sha256','counts')},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();export(a.package,a.out)
