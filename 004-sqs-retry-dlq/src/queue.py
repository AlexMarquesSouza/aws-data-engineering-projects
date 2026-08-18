"""Simula recebimentos SQS, retentativas e redrive para DLQ."""
from __future__ import annotations
import argparse,json
from collections import deque
from pathlib import Path
def executar(entrada:Path,saida:Path,max_receives:int=3)->dict:
 fila=deque({**json.loads(x),"receive_count":0} for x in entrada.read_text().splitlines() if x.strip());ok=[];dlq=[];tentativas=[]
 while fila:
  m=fila.popleft();m["receive_count"]+=1;tentativas.append({"message_id":m["message_id"],"attempt":m["receive_count"]})
  sucesso=m["kind"]=="valid" or (m["kind"]=="transient" and m["receive_count"]>=2)
  if sucesso:ok.append(m);continue
  if m["receive_count"]>=max_receives:dlq.append(m)
  else:fila.append(m)
 resultado={"processed":[m["message_id"] for m in ok],"dead_letter":[m["message_id"] for m in dlq],"attempts":tentativas};saida.mkdir(parents=True,exist_ok=True);(saida/"result.json").write_text(json.dumps(resultado,indent=2)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/messages.jsonl"));p.add_argument("--output",type=Path,default=Path("data/output"));p.add_argument("--max-receives",type=int,default=3);a=p.parse_args();print(json.dumps(executar(a.input,a.output,a.max_receives),indent=2))
if __name__=="__main__":main()
