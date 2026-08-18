"""Compara candidatas a partition key por concentração de tráfego."""
from __future__ import annotations
import argparse,csv,json
from collections import defaultdict
from pathlib import Path
def executar(entrada:Path,saida:Path)->dict:
 with entrada.open(newline="",encoding="utf-8") as f:rows=list(csv.DictReader(f))
 resultados=[]
 for campo in ("user_id","status","event_date"):
  carga=defaultdict(int)
  for r in rows:carga[r[campo]]+=int(r["rcu"])
  total=sum(carga.values());maior=max(carga.values());resultados.append({"key":campo,"distinct_values":len(carga),"hottest_share_pct":round(maior/total*100,2),"risk":"high" if maior/total>.5 else "acceptable"})
 resultados.sort(key=lambda x:(x["risk"]=="high",x["hottest_share_pct"]));resultado={"recommended":resultados[0]["key"],"candidates":resultados};saida.parent.mkdir(parents=True,exist_ok=True);saida.write_text(json.dumps(resultado,indent=2)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/requests.csv"));p.add_argument("--output",type=Path,default=Path("data/output/hotkeys.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
