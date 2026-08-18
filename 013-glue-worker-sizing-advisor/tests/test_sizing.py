import unittest
from src.sizing import recommend
class TestSizing(unittest.TestCase):
    def test_small_general_job(self):
        r=recommend({"name":"a","input_gb":20,"memory_bound":False}); self.assertEqual(r["worker_type"],"G.1X"); self.assertEqual(r["number_of_workers"],2)
    def test_memory_job(self): self.assertEqual(recommend({"name":"a","input_gb":100,"memory_bound":True})["worker_type"],"R.1X")
    def test_large_job(self): self.assertEqual(recommend({"name":"a","input_gb":800,"memory_bound":False})["worker_type"],"G.4X")
if __name__=="__main__": unittest.main()
