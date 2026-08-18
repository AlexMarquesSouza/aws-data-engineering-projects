import tempfile,unittest
from pathlib import Path
from src.planner import executar
class T(unittest.TestCase):
 def test_plan(self):
  r=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   x=executar(r/"data/producers.csv",Path(t)/"r.json");self.assertEqual(x["minimum_shards"],2);self.assertEqual(x["partition_key_risks"],["partner"])
