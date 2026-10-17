import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'publication'))
from audit_release import audit, bilingual, validate
from verify_release import assert_equivalent


class PublicationAuditTests(unittest.TestCase):
    def setUp(self):
        with tempfile.TemporaryDirectory() as name:
            p=Path(name)
            (p/'questions.json').write_bytes((ROOT/'questions.en.original.json').read_bytes())
            self.q=next(q for q in bilingual.inventory(p) if q['id']=='legal-07')
        self.image={'id':'abc','png_sha256':'imagehash','race':0,'gender':0,'age':40}

    def record(self, answer, model='jev'):
        q=self.q
        served='jev-1.14.0' if model=='jev' else 'gpt-6-luna'
        body={'model':served,'answers':{'audit':answer}}
        return {**self.image,'image_id':self.image['id'],'question_id':q['id'],
            'model':model,'requested_model':audit.MODELS[model][1],'repeat':0,
            'task_id':audit.task_key(self.image,q,model,audit.MODELS[model][1],0,2),
            'prompt_sha256':audit.digest(q['prompt'].encode()),'expected':q['expected'],
            'adverse':q.get('adverse'),**audit.normalize(model,body,q)}

    def test_legacy_metadata_is_recovered_only_from_matching_task_and_prompt(self):
        r=self.record({'type':'choice','choice':'Cannot tell','probabilities':{'Criminal':0,'Law-abiding Civilian':0,'Cannot tell':1}})
        self.assertFalse(validate(r,self.image,self.q)['refusal'])
        r['prompt_sha256']='tampered'
        with self.assertRaisesRegex(AssertionError,'Prompt mismatch'):
            validate(r,self.image,self.q)

    def test_explicit_refusal_is_preserved_but_unknown_answer_fails(self):
        r=self.record({'type':'refusal','reason':'policy'},'gpt-decisions')
        self.assertTrue(validate(r,self.image,self.q)['refusal'])
        r=self.record({'type':'unexpected'},'gpt-decisions')
        with self.assertRaisesRegex(AssertionError,'Unknown unscored'):
            validate(r,self.image,self.q)

    def test_changing_normalized_choice_without_changing_raw_response_fails(self):
        r=self.record({'type':'choice','choice':'Cannot tell','probabilities':{'Criminal':0,'Law-abiding Civilian':0,'Cannot tell':1}})
        r['choice']='Criminal'
        with self.assertRaisesRegex(AssertionError,'Normalizer discrepancy'):
            validate(r,self.image,self.q)

    def test_score_discrepancy_is_observed_without_overwriting_decision(self):
        r=self.record({'type':'choice','choice':'Cannot tell','probabilities':{'Criminal':.03,'Law-abiding Civilian':.49,'Cannot tell':.48}})
        result=validate(r,self.image,self.q)
        self.assertAlmostEqual(result['argmax_deficit'],.01)
        self.assertEqual(r['choice'],'Cannot tell')

    def test_invalid_probability_vector_fails_even_when_choice_is_allowed(self):
        r=self.record({'type':'choice','choice':'Cannot tell','probabilities':{'Criminal':.2,'Law-abiding Civilian':.3,'Cannot tell':.7}})
        with self.assertRaisesRegex(AssertionError,'Invalid probability'):
            validate(r,self.image,self.q)

    def test_served_model_drift_fails(self):
        r=self.record({'type':'choice','choice':'Cannot tell','probabilities':{'Criminal':0,'Law-abiding Civilian':0,'Cannot tell':1}})
        r['raw_response']['model']='other-version'
        r.update(audit.normalize('jev',r['raw_response'],self.q))
        with self.assertRaisesRegex(AssertionError,'served version'):
            validate(r,self.image,self.q)

    def test_cross_version_float_tolerance_does_not_relax_counts_or_structure(self):
        assert_equivalent({'n':1497,'p':.020980661693762486},{'n':1497,'p':.02098066169376244})
        for changed in ({'n':1496,'p':.020980661693762486},{'n':1497,'p':.02099},{'n':1497}):
            with self.assertRaises(AssertionError):
                assert_equivalent(changed,{'n':1497,'p':.020980661693762486})


if __name__=='__main__': unittest.main()
