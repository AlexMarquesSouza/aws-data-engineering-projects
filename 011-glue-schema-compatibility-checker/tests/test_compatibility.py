import unittest
from src.compatibility import check
class TestCompatibility(unittest.TestCase):
    def setUp(self): self.old={"fields":[{"name":"id","type":"string"}]}
    def test_optional_field(self): self.assertTrue(check(self.old,{"fields":[{"name":"id","type":"string"},{"name":"note","type":["null","string"]}]})["compatible"])
    def test_required_field(self): self.assertFalse(check(self.old,{"fields":[{"name":"id","type":"string"},{"name":"total","type":"double"}]})["compatible"])
    def test_changed_type(self): self.assertFalse(check(self.old,{"fields":[{"name":"id","type":"long"}]})["compatible"])
if __name__=="__main__": unittest.main()
