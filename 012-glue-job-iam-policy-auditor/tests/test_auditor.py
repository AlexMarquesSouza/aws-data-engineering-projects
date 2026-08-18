import unittest
from src.auditor import audit
class TestAuditor(unittest.TestCase):
    def test_scoped(self): self.assertTrue(audit({"Statement":[{"Effect":"Allow","Action":"s3:GetObject","Resource":"arn:aws:s3:::bucket/raw/*"}]})["compliant"])
    def test_wildcards(self): self.assertEqual(len(audit({"Statement":[{"Effect":"Allow","Action":"glue:*","Resource":"*"}]})["findings"]),2)
    def test_passrole_condition(self):
        p={"Statement":[{"Effect":"Allow","Action":"iam:PassRole","Resource":"arn:aws:iam::1:role/glue"}]}; self.assertEqual(audit(p)["findings"][0]["severity"],"MEDIUM")
if __name__=="__main__": unittest.main()
