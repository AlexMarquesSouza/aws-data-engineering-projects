import argparse, csv, json
from pathlib import Path
def audit(rows,sensitive):
    findings=[]
    for row in rows:
        resource=f'{row["database"]}.{row["table"]}'; columns={x.strip() for x in row["columns"].split(";") if x.strip()}; exposed=sorted(sensitive.get(resource,set()) & columns)
        if row["permission"]=="SELECT" and row["columns"].strip()=="*": findings.append({"severity":"HIGH","principal":row["principal"],"resource":resource,"reason":"SELECT sem filtro de colunas"})
        elif exposed: findings.append({"severity":"MEDIUM","principal":row["principal"],"resource":resource,"reason":"Colunas sensíveis: "+", ".join(exposed)})
    return {"compliant":not findings,"grants_checked":len(rows),"findings":findings}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--permissions",default="data/permissions.csv"); p.add_argument("--policy",default="data/policy.json"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args()
    with open(a.permissions,encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    raw=json.loads(Path(a.policy).read_text(encoding="utf-8")); report=audit(rows,{k:set(v) for k,v in raw["sensitive_columns"].items()}); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(report,ensure_ascii=False,indent=2)); raise SystemExit(0 if report["compliant"] else 2)
if __name__=="__main__": main()
