"""Compara o cabeçalho recebido com um contrato antes do Glue Crawler."""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
def executar(entrada:Path,contrato:Path,relatorio:Path)->dict:
 esperado=list(json.loads(contrato.read_text(encoding="utf-8")))
 with entrada.open(newline="",encoding="utf-8") as f:recebido=next(csv.reader(f))
 novos=[c for c in recebido if c not in esperado];ausentes=[c for c in esperado if c not in recebido];ordem_alterada=not novos and not ausentes and recebido!=esperado
 status="breaking" if ausentes else ("additive" if novos else ("reordered" if ordem_alterada else "compatible"))
 resultado={"status":status,"esperado":esperado,"recebido":recebido,"novos":novos,"ausentes":ausentes,"ordem_alterada":ordem_alterada}
 relatorio.parent.mkdir(parents=True,exist_ok=True);relatorio.write_text(json.dumps(resultado,indent=2,ensure_ascii=False)+"\n",encoding="utf-8");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/input/orders.csv"));p.add_argument("--contract",type=Path,default=Path("contracts/orders.json"));p.add_argument("--report",type=Path,default=Path("data/output/schema-report.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.contract,a.report),indent=2))
if __name__=="__main__":main()
