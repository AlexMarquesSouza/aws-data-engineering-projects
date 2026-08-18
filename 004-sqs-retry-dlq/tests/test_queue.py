import tempfile,unittest
from pathlib import Path
from src.queue import executar
class TestQueue(unittest.TestCase):
 def test_retry_transitorio_e_dlq(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"data/messages.jsonl",Path(t));self.assertEqual(r["processed"],["m1","m2"]);self.assertEqual(r["dead_letter"],["m3"]);self.assertEqual(len([x for x in r["attempts"] if x["message_id"]=="m3"]),3)
if __name__=="__main__":unittest.main()
