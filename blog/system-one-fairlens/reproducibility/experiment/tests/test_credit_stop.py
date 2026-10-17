import io,json,sys,tempfile,unittest,urllib.error
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import audit

BODY=json.dumps({'error':{'type':'insufficient_quota','code':'credit_balance_exhausted'}}).encode()

def failure():
    return urllib.error.HTTPError('https://api.openai.com/v1/decisions',429,'quota',{},io.BytesIO(BODY))

class CreditStopTests(unittest.TestCase):
    def test_credit_exhaustion_is_not_retried_and_error_body_survives(self):
        q={'prompt':'p','choices':['Yes','No']}
        with patch('audit.urllib.request.urlopen',side_effect=failure()) as call,patch('audit.time.sleep') as sleep:
            with self.assertRaises(urllib.error.HTTPError) as exc:
                audit.query('gpt-decisions',b'png',q,'fake','gpt-6-luna')
            self.assertTrue(audit.credits_exhausted(exc.exception.read()))
            self.assertEqual(call.call_count,1)
            sleep.assert_not_called()

    def test_quota_stops_run_after_checkpoint_before_next_task(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            (root/'img.png').write_bytes(b'pixels')
            m={'provenance':{},'images':[{'id':'a','image':'img.png','png_sha256':audit.digest(b'pixels'),'race':0,'gender':0,'age':35}],
               'questions':[{'id':str(i),'prompt':str(i),'choices':['Yes','No'],'expected':'Yes'} for i in range(2)]}
            audit.dump(root/'manifest.json',m)
            with patch.dict('os.environ',{'OPENAI_API_KEY':'fake'}),patch('audit.query',side_effect=failure()) as call:
                with self.assertRaisesRegex(RuntimeError,'API_CREDITS_EXHAUSTED'):
                    audit.run(root,root/'out',['gpt-decisions'],0,1,1,2,False)
                self.assertEqual(call.call_count,1)
            records=audit.latest_records((root/'out').glob('predictions-*.jsonl'))
            self.assertEqual(len(records),1)
            self.assertEqual(next(iter(records.values()))['fatal_error'],'credits_exhausted')
