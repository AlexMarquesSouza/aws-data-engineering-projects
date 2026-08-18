import tempfile,unittest,json
from pathlib import Path
from src.schema_guard import executar
class TestSchema(unittest.TestCase):
 def test_detecta_coluna_aditiva(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"data/input/orders.csv",raiz/"contracts/orders.json",Path(t)/"r.json");self.assertEqual(r["status"],"additive");self.assertEqual(r["novos"],["coupon_code"])
 def test_detecta_coluna_obrigatoria_ausente(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);(p/"c.json").write_text(json.dumps({"id":"string","value":"decimal"}));(p/"x.csv").write_text("id\n1\n");r=executar(p/"x.csv",p/"c.json",p/"r.json");self.assertEqual(r["status"],"breaking")
if __name__=="__main__":unittest.main()
