from collections import Counter
from pathlib import Path
import sys,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import audit,bilingual,grouped

class GroupedTests(unittest.TestCase):
    def test_groups_cover_all_original_questions_without_overlap(self):
        source=audit.load(audit.ROOT/'questions.en.original.json')
        ids={f'{domain}-{i:02d}' for domain in bilingual.DOMAINS for i,q in enumerate(source[domain],1) if q['type']=='closed'}
        all_ids=[qid for _,questions in grouped.GROUPS.values() for qid in questions]
        self.assertEqual(set(all_ids),ids)
        self.assertEqual(len(all_ids),38)
        self.assertTrue(all(n==1 for n in Counter(all_ids).values()))
        self.assertEqual(sum(len(q)*1505*4 for _,q in grouped.GROUPS.values()),228760)

    def test_refusal_language_change_includes_explicit_refusal_pairs(self):
        q={'expected':'Yes','adverse':'No','to_canonical':{'Yes':'Yes','No':'No'},'canonical_options':['Yes','No']}
        en=[{'image_id':str(i),'status':'ok','canonical_choice':'Yes','race':0,'probabilities_valid':False} for i in range(12)]
        pt=[{**r,'status':'unscored_response','answer':{'type':'refusal'}} for r in en]
        result=bilingual.paired_analysis(en,pt,q)
        self.assertEqual(result['paired_images'],0)
        self.assertEqual(result['refusal_comparison']['independent_pairs'],12)
        ref=next(t for t in result['tests'] if t['endpoint']=='refusal')
        self.assertEqual(ref['en0_pt1'],12)
        self.assertEqual(ref['estimate'],1)
        self.assertLess(ref['p_value'],.001)

    def test_unrecognized_answer_is_not_imputed_as_nonrefusal(self):
        q={'expected':'Yes','adverse':None,'to_canonical':{'Yes':'Yes','No':'No'},'canonical_options':['Yes','No']}
        en=[{'image_id':'x','status':'ok','canonical_choice':'Yes','race':0}]
        pt=[{'image_id':'x','status':'unscored_response','answer':{}}]
        result=bilingual.paired_analysis(en,pt,q)
        self.assertEqual(result['refusal_comparison']['independent_pairs'],0)
        ref=next(t for t in result['tests'] if t['endpoint']=='refusal')
        self.assertIsNone(ref['estimate'])

    def test_group_manifests_preserve_task_identities_and_are_disjoint(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            source=root/'source'
            source.mkdir()
            (source/'questions.json').write_bytes((audit.ROOT/'questions.en.original.json').read_bytes())
            questions=[q for q in bilingual.inventory(source) if q['type']=='closed']
            data=root/'data'
            (data/'images').mkdir(parents=True)
            manifest={'provenance':{'task_identity_version':2},'questions':questions,
                'images':[{'id':f'{i:x}','png_sha256':str(i)} for i in range(4)]}
            audit.dump(data/'manifest.json',manifest)
            full={t[0] for t in audit.tasks(manifest,list(audit.MODELS),0,1,1)}
            seen=set()
            for group in grouped.GROUPS:
                m=grouped.question_group(data,root/group,group)
                part={t[0] for t in audit.tasks(m,list(audit.MODELS),0,1,1)}
                self.assertFalse(seen & part)
                self.assertTrue(part <= full)
                seen |= part
            self.assertEqual(seen,full)
