import unittest
from src.audit import audit
class TestAudit(unittest.TestCase):
    def test_compliant(self): self.assertTrue(audit([{"principal":"p","database":"db","table":"t","permission":"SELECT","columns":"id;total"}],{"db.t":{"email"}})["compliant"])
    def test_findings(self):
        rows=[{"principal":"p1","database":"db","table":"t","permission":"SELECT","columns":"*"},{"principal":"p2","database":"db","table":"t","permission":"SELECT","columns":"id;email"}]; r=audit(rows,{"db.t":{"email"}}); self.assertFalse(r["compliant"]); self.assertEqual(len(r["findings"]),2)
if __name__=="__main__": unittest.main()
