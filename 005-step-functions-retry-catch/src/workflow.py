"""Executa workflow ETL local com Retry e Catch determinísticos."""
from __future__ import annotations
import argparse,json
from pathlib import Path
class TaskError(Exception):pass
def executar(saida:Path,modo:str="transient",max_attempts:int=3)->dict:
 historico=[{"state":"Extract","status":"Succeeded"}];attempt=0;transformado=False
 while attempt<max_attempts:
  attempt+=1
  if modo=="success" or (modo=="transient" and attempt>=2):transformado=True;historico.append({"state":"Transform","attempt":attempt,"status":"Succeeded"});break
  historico.append({"state":"Transform","attempt":attempt,"status":"Failed"})
 if transformado:historico.append({"state":"Load","status":"Succeeded"});status="SUCCEEDED"
 else:historico.append({"state":"NotifyFailure","status":"Succeeded"});status="CAUGHT_FAILURE"
 resultado={"status":status,"attempts":attempt,"history":historico};saida.parent.mkdir(parents=True,exist_ok=True);saida.write_text(json.dumps(resultado,indent=2)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=Path("data/output/execution.json"));p.add_argument("--mode",choices=["success","transient","permanent"],default="transient");a=p.parse_args();print(json.dumps(executar(a.output,a.mode),indent=2))
if __name__=="__main__":main()
