import tempfile,unittest
from pathlib import Path
from src.workflow import executar
class TestWorkflow(unittest.TestCase):
 def test_retry_recupera_falha_transitoria(self):
  with tempfile.TemporaryDirectory() as t:
   r=executar(Path(t)/"r.json","transient");self.assertEqual(r["status"],"SUCCEEDED");self.assertEqual(r["attempts"],2)
 def test_catch_trata_falha_permanente(self):
  with tempfile.TemporaryDirectory() as t:
   r=executar(Path(t)/"r.json","permanent");self.assertEqual(r["status"],"CAUGHT_FAILURE");self.assertEqual(r["history"][-1]["state"],"NotifyFailure")
if __name__=="__main__":unittest.main()
