import argparse,csv,json,math
from pathlib import Path
def executar(inp,out):
 with inp.open(newline="",encoding="utf-8") as f:r=list(csv.DictReader(f))
 rec=sum(int(x["records_per_second"]) for x in r);kb=sum(int(x["records_per_second"])*float(x["kb_per_record"]) for x in r);shards=max(math.ceil(rec/1000),math.ceil(kb/1024));risks=[x["producer"] for x in r if int(x["partition_keys"])<shards*10];res={"records_per_second":rec,"kb_per_second":kb,"minimum_shards":shards,"partition_key_risks":risks};out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(res,indent=2)+"\n");return res
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/producers.csv"));p.add_argument("--output",type=Path,default=Path("data/output/plan.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
