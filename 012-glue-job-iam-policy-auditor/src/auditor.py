import argparse,json
from pathlib import Path
def values(value): return value if isinstance(value,list) else [value]
def audit(policy):
    findings=[]
    for index,stmt in enumerate(policy.get("Statement",[]),1):
        if stmt.get("Effect")!="Allow": continue
        actions=values(stmt.get("Action",[])); resources=values(stmt.get("Resource",[]))
        if "*" in actions or any(x.endswith(":*") for x in actions): findings.append({"statement":index,"severity":"HIGH","reason":"ações curingas"})
        if "*" in resources: findings.append({"statement":index,"severity":"HIGH","reason":"recursos curingas"})
        if "iam:PassRole" in actions and not stmt.get("Condition"): findings.append({"statement":index,"severity":"MEDIUM","reason":"iam:PassRole sem Condition"})
    return {"compliant":not findings,"statements_checked":len(policy.get("Statement",[])),"findings":findings}
def main():
    p=argparse.ArgumentParser(); p.add_argument("input",nargs="?",default="data/glue-job-policy.json"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args(); report=audit(json.loads(Path(a.input).read_text())); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n"); print(json.dumps(report,ensure_ascii=False,indent=2)); raise SystemExit(0 if report["compliant"] else 2)
if __name__=="__main__": main()
