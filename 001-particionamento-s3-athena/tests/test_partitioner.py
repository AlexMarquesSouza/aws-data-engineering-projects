import tempfile,unittest
from pathlib import Path
from src.partitioner import executar
class TestParticao(unittest.TestCase):
 def test_cria_tres_particoes_hive(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   out=Path(t);r=executar(raiz/"data/input/eventos.csv",out);self.assertEqual(r["particoes"],3);self.assertEqual(r["registros"],4);self.assertTrue((out/"year=2026/month=08/day=04").is_dir())
if __name__=="__main__":unittest.main()
