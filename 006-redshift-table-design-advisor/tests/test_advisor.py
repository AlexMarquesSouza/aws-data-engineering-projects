import tempfile,unittest
from pathlib import Path
from src.advisor import executar
class TestAdvisor(unittest.TestCase):
 def test_sugere_colocacao_e_filtro_temporal(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"data/workload.json",Path(t)/"r.json");self.assertEqual(r["diststyle"],"KEY");self.assertEqual(r["distkey"],"customer_id");self.assertEqual(r["sortkey"],"sale_date");self.assertIn("DISTKEY(customer_id)",r["ddl_draft"])
if __name__=="__main__":unittest.main()
