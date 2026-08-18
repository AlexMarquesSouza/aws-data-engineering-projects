import argparse,csv,json
from collections import Counter
from pathlib import Path
def executar(inp,out):
 with inp.open(newline="",encoding="utf-8") as f:r=list(csv.DictReader(f))
 ids=Counter(x["order_id"] for x in r);checks={"IsComplete.order_id":all(x["order_id"] for x in r),"IsUnique.order_id":all(v==1 for v in ids.values()),"IsComplete.customer_id":all(x["customer_id"] for x in r),"ColumnValues.amount>0":all(float(x["amount"])>0 for x in r)};passed=sum(checks.values());res={"score_pct":passed/len(checks)*100,"checks":checks};out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(res,indent=2)+"\n");return res
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/orders.csv"));p.add_argument("--output",type=Path,default=Path("data/output/report.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
