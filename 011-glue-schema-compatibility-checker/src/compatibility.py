import argparse, json
from pathlib import Path
def fields(schema): return {x["name"]:x for x in schema.get("fields",[])}
def is_optional(field): return isinstance(field.get("type"),list) and "null" in field["type"]
def check(old,new,mode="BACKWARD"):
    before,after=fields(old),fields(new); issues=[]
    if mode=="DISABLED": issues.append("Versionamento desabilitado")
    elif mode in {"BACKWARD","BACKWARD_ALL","FULL","FULL_ALL"}:
        for name,field in before.items():
            if name not in after: issues.append(f"Campo removido: {name}")
            elif after[name]["type"]!=field["type"]: issues.append(f"Tipo alterado: {name}")
        for name,field in after.items():
            if name not in before and not is_optional(field) and "default" not in field: issues.append(f"Novo campo obrigatório sem default: {name}")
    return {"compatible":not issues,"mode":mode,"issues":issues,"old_fields":len(before),"new_fields":len(after)}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--old",default="data/order-v1.avsc"); p.add_argument("--new",default="data/order-v2.avsc"); p.add_argument("--mode",default="BACKWARD"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args(); report=check(json.loads(Path(a.old).read_text()),json.loads(Path(a.new).read_text()),a.mode); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n"); print(json.dumps(report,ensure_ascii=False,indent=2)); raise SystemExit(0 if report["compatible"] else 2)
if __name__=="__main__": main()
