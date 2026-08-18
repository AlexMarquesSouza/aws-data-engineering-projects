import tempfile,unittest
from pathlib import Path
from src.bookmark_job import executar
class TestBookmark(unittest.TestCase):
 def test_reexecucao_nao_reprocessa(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);a=executar(raiz/"data/input/customers.csv",p/"out.csv",p/"state.json");b=executar(raiz/"data/input/customers.csv",p/"out.csv",p/"state.json");self.assertEqual(a["processados"],3);self.assertEqual(b["processados"],0);self.assertEqual(b["bookmark_atual"],"c-3")
if __name__=="__main__":unittest.main()
