import tempfile,unittest
from pathlib import Path
from src.quality import executar
class T(unittest.TestCase):
 def test_rules(self):
  r=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   x=executar(r/"data/orders.csv",Path(t)/"r.json");self.assertEqual(x["score_pct"],25);self.assertTrue(x["checks"]["IsComplete.order_id"])
