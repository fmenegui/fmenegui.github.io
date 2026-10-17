from collections import Counter
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import audit
import bilingual as b

class BilingualTests(unittest.TestCase):
    def inventory(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'questions.json').write_bytes((audit.ROOT/'questions.en.original.json').read_bytes())
            return b.inventory(p)

    def test_all_original_questions_and_translations_preserve_option_semantics(self):
        rows=self.inventory()
        self.assertEqual(len(rows),138)
        self.assertEqual(Counter((q['language'],q['type']) for q in rows),
                         {('en','closed'):38,('pt-BR','closed'):38,('en','open'):31,('pt-BR','open'):31})
        en={q['base_id']:q for q in rows if q['language']=='en'}
        for q in rows:
            if q['type']=='closed':
                self.assertEqual([q['to_canonical'][v] for v in q['choices']],en[q['base_id']]['choices'])
                self.assertEqual(q['to_canonical'][q['expected']],en[q['base_id']]['expected'])
                if q.get('adverse'):
                    self.assertEqual(q['to_canonical'][q['adverse']],en[q['base_id']]['adverse'])
            else:
                self.assertEqual(q['capability_status'],'unsupported_free_text')
                self.assertNotIn('choices',q)
        self.assertIsNone(en['hiring-15']['adverse'])

    def test_source_drift_stops_before_calls(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            data=audit.load(audit.ROOT/'questions.en.original.json')
            data['legal'][0]['text']+=' changed'
            audit.dump(p/'questions.json',data)
            with self.assertRaisesRegex(ValueError,'differs'):
                b.inventory(p)

    def test_original_legal_english_payload_and_cache_identity_unchanged(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'questions.json').write_bytes((audit.ROOT/'questions.en.original.json').read_bytes())
            old=audit.questions(p)
            new={q['id']:q for q in b.inventory(p)}
            for q in old:
                self.assertEqual(audit.payload('jev',b'png',q,'jev-preview'),
                                 audit.payload('jev',b'png',new[q['id']],'jev-preview'))
                m={'images':[{'id':'abc','png_sha256':'x'}],'questions':[q]}
                n={**m,'questions':[new[q['id']]]}
                self.assertEqual([t[0] for t in audit.tasks(m,list(audit.MODELS),0,1,1)],
                                 [t[0] for t in audit.tasks(n,list(audit.MODELS),0,1,1)])

    def test_zero_events_does_not_imply_zero_uncertainty(self):
        gap=b.newcombe([0]*353,[0]*622)
        self.assertEqual(gap['estimate'],0)
        self.assertLess(gap['ci95'][0],0)
        self.assertGreater(gap['ci95'][1],0)
        self.assertIsNone(b.newcombe([],[])['ci95'])

    def test_paired_language_alignment_is_by_image_not_input_order(self):
        q=next(q for q in self.inventory() if q['id']=='legal-07')
        def row(i,choice,prob):
            return {'image_id':str(i),'status':'ok','canonical_choice':choice,'race':i%2,
                    'probabilities_valid':True,'canonical_probabilities':{'Criminal':prob}}
        en=[row(i,'Cannot tell',.1) for i in range(20)]
        pt=list(reversed([row(i,'Criminal',.3) for i in range(20)]))
        result=b.paired_analysis(en,pt,q)
        self.assertEqual(result['paired_images'],20)
        self.assertEqual(result['changed_choice_n'],20)
        test=next(r for r in result['tests'] if r['endpoint']=='adverse')
        self.assertEqual(test['en0_pt1'],20)
        self.assertEqual(test['en1_pt0'],0)
        self.assertAlmostEqual(test['estimate'],1)
        self.assertLess(test['p_value'],.00001)
        self.assertAlmostEqual(result['adverse_score_change']['estimate'],.2)
        self.assertAlmostEqual(result['race_by_language_score_interaction']['estimate'],0)

    def test_missing_or_refused_partner_is_not_imputed(self):
        q=next(q for q in self.inventory() if q['id']=='hiring-15')
        row={'image_id':'x','status':'ok','canonical_choice':'Cannot tell','race':0}
        result=b.paired_analysis([row],[{**row,'status':'unscored_response'}],q)
        self.assertEqual(result['paired_images'],0)
        self.assertIsNone(result['tests'][0]['estimate'])
        self.assertNotIn('adverse_score_change',result)
        summary=b.summarize([{**row,'probabilities_valid':False}],q)
        self.assertIsNone(summary['adverse_rate'])
        self.assertEqual(summary['non_neutral_rate'],0)

    def test_holm_corrects_entire_language_test_family(self):
        rows=[{'p_value':v} for v in (.04,.001,.03)]
        b.holm(rows)
        self.assertEqual([r['family_size'] for r in rows],[3]*3)
        self.assertAlmostEqual(rows[1]['p_holm'],.003)
        self.assertAlmostEqual(rows[0]['p_holm'],.06)
        self.assertAlmostEqual(rows[2]['p_holm'],.06)

    def test_all_languages_models_questions_stay_in_same_image_shard(self):
        q=[q for q in self.inventory() if q['type']=='closed']
        m={'images':[{'id':f'{i:x}','png_sha256':str(i)} for i in range(1505)],'questions':q}
        counts=[]
        seen=set()
        for shard in range(64):
            part=audit.tasks(m,list(audit.MODELS),shard,64,1)
            ids={t[0] for t in part}
            self.assertFalse(seen & ids)
            seen |= ids
            counts.append(len(part))
        self.assertEqual(len(seen),228760)
        self.assertEqual(sum(counts),228760)
        self.assertTrue(all(c%152==0 for c in counts))

if __name__=='__main__':
    unittest.main()

class PersistenceTests(unittest.TestCase):
    def test_seed_requires_exact_identity_and_keeps_only_shard(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            q={'id':'legal-07','prompt':'prompt','choices':['Yes','No'],'expected':'No','adverse':'Yes'}
            m={'images':[{'id':'a','png_sha256':'sha'}],'questions':[q]}
            audit.dump(root/'data/manifest.json',m)
            task=audit.tasks(m,['jev'],0,1,1)[0][0]
            seed=root/'old'
            seed.mkdir()
            row={'task_id':task,'status':'ok','image_id':'a','png_sha256':'sha','prompt_sha256':audit.digest(b'prompt'),'served_model':'jev-1.14.0'}
            (seed/'predictions-test.jsonl').write_text(json.dumps(row)+'\n'+json.dumps({**row,'task_id':'unrelated'})+'\n')
            result=b.seed(root/'data',root/'out',[seed])
            self.assertEqual(result['seeded_exact_tasks'],1)
            self.assertEqual(set(audit.latest_records((root/'out').glob('predictions-*.jsonl'))),{task})
            result=b.seed(root/'data',root/'other',[seed],1,2)
            self.assertEqual(result['seeded_exact_tasks'],0)

    def test_model_drift_is_checkpointed_as_nonterminal_failure(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            q={'id':'x','prompt':'p','choices':['Yes','No'],'expected':'Yes'}
            (root/'img.png').write_bytes(b'pixels')
            m={'provenance':{},'images':[{'id':'a','image':'img.png','png_sha256':audit.digest(b'pixels'),'race':0,'gender':0,'age':35}],'questions':[q]}
            audit.dump(root/'manifest.json',m)
            with patch.dict('os.environ',{'JEV_API_KEY':'fake','EXPECTED_JEV_SERVED_MODEL':'jev-1.14.0'}),patch('audit.query',return_value={'status':'ok','served_model':'changed'}):
                with self.assertRaisesRegex(RuntimeError,'model changed'):
                    audit.run(root,root/'out',['jev'],0,1,1,1,False)
            r=next(iter(audit.latest_records((root/'out').glob('predictions-*.jsonl')).values()))
            self.assertEqual(r['status'],'model_version_mismatch')
            self.assertIsNone(r['adverse'])

class DuplicateTests(unittest.TestCase):
    def test_duplicate_pixels_remain_distinct_official_tasks_in_v2(self):
        q={'id':'q','prompt':'p','choices':['Yes','No'],'expected':'Yes'}
        m={'provenance':{'task_identity_version':2},'images':[{'id':i,'png_sha256':'same'} for i in ('a','b')],'questions':[q]}
        self.assertEqual(len({t[0] for t in audit.tasks(m,['jev'],0,1,1)}),2)

    def test_duplicate_or_ambiguous_inputs_do_not_multiply_independent_pairs(self):
        q={'expected':'Cannot tell','adverse':'Criminal','to_canonical':{'Cannot tell':'Cannot tell','Criminal':'Criminal'},'canonical_options':['Criminal','Cannot tell']}
        en=[{'image_id':str(i),'png_sha256':'same' if i<3 else 'ambiguous','demographic_ambiguous':i==3,
             'status':'ok','canonical_choice':'Cannot tell','race':0,'probabilities_valid':False} for i in range(4)]
        pt=[{**r,'canonical_choice':'Criminal'} for r in en]
        result=b.paired_analysis(en,pt,q)
        self.assertEqual(result['paired_images'],4)
        self.assertEqual(result['independent_image_pairs'],1)
        self.assertEqual(result['changed_choice_n'],4)
        self.assertEqual(result['tests'][0]['n'],1)
