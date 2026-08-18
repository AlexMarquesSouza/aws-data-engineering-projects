"""Simula um AWS Glue job bookmark baseado em chave crescente."""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
def executar(entrada:Path,saida:Path,estado:Path)->dict:
 anterior=json.loads(estado.read_text())["last_customer_id"] if estado.exists() else ""
 with entrada.open(newline="",encoding="utf-8") as f:
  leitor=csv.DictReader(f);novos=[r for r in leitor if r["customer_id"]>anterior]
 novos.sort(key=lambda r:r["customer_id"]);saida.parent.mkdir(parents=True,exist_ok=True)
 with saida.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=["customer_id","name","updated_at"]);w.writeheader();w.writerows(novos)
 atual=novos[-1]["customer_id"] if novos else anterior;estado.parent.mkdir(parents=True,exist_ok=True);estado.write_text(json.dumps({"last_customer_id":atual},indent=2)+"\n")
 return {"bookmark_anterior":anterior,"bookmark_atual":atual,"processados":len(novos)}
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/input/customers.csv"));p.add_argument("--output",type=Path,default=Path("data/output/customers_delta.csv"));p.add_argument("--state",type=Path,default=Path("state/bookmark.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output,a.state),indent=2))
if __name__=="__main__":main()
