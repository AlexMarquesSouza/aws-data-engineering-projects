import tempfile,unittest
from pathlib import Path
from src.hotkey import executar
class TestHotkey(unittest.TestCase):
 def test_rejeita_data_e_status_concentrados(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"data/requests.csv",Path(t)/"r.json");self.assertEqual(r["recommended"],"user_id");self.assertEqual(next(x for x in r["candidates"] if x["key"]=="event_date")["hottest_share_pct"],100.0)
if __name__=="__main__":unittest.main()
