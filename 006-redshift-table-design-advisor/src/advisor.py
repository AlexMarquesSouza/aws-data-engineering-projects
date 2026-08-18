"""Gera sugestão inicial de distribuição e sort key pelo workload."""
from __future__ import annotations
import argparse,json
from pathlib import Path
def executar(entrada:Path,saida:Path)->dict:
 w=json.loads(entrada.read_text());join=max(w["join_columns"],key=w["join_columns"].get,default=None);filtro=max(w["filter_columns"],key=w["filter_columns"].get,default=None)
 if w["size_gb"]<1 and w["updates_per_day"]<1000:dist="ALL";distkey=None
 elif join and w["join_columns"][join]>=50:dist="KEY";distkey=join
 else:dist="AUTO";distkey=None
 ddl=f"CREATE TABLE {w['table']} (...) DISTSTYLE {dist}"+(f" DISTKEY({distkey})" if distkey else "")+(f" SORTKEY({filtro});" if filtro else ";")
 resultado={"table":w["table"],"diststyle":dist,"distkey":distkey,"sortkey":filtro,"ddl_draft":ddl,"warning":"Validar com EXPLAIN e workload real"};saida.parent.mkdir(parents=True,exist_ok=True);saida.write_text(json.dumps(resultado,indent=2)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/workload.json"));p.add_argument("--output",type=Path,default=Path("data/output/recommendation.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
