"""Organiza eventos em prefixos Hive compatíveis com S3/Athena."""
from __future__ import annotations
import argparse,csv,hashlib,json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

def executar(entrada:Path,saida:Path)->dict:
    grupos=defaultdict(list)
    with entrada.open(newline="",encoding="utf-8") as f:
        leitor=csv.DictReader(f)
        if leitor.fieldnames != ["evento_id","ocorrido_em","tipo","usuario_id"]: raise ValueError("schema inesperado")
        for linha in leitor:
            dt=datetime.fromisoformat(linha["ocorrido_em"].replace("Z","+00:00")); grupos[(dt.year,dt.month,dt.day)].append(linha)
    arquivos=[]
    for (ano,mes,dia),linhas in sorted(grupos.items()):
        pasta=saida/f"year={ano:04d}"/f"month={mes:02d}"/f"day={dia:02d}"; pasta.mkdir(parents=True,exist_ok=True)
        digest=hashlib.sha256(json.dumps(linhas,sort_keys=True).encode()).hexdigest()[:10]; alvo=pasta/f"eventos-{digest}.csv"
        with alvo.open("w",newline="",encoding="utf-8") as f: w=csv.DictWriter(f,fieldnames=["evento_id","ocorrido_em","tipo","usuario_id"]); w.writeheader(); w.writerows(linhas)
        arquivos.append({"arquivo":str(alvo),"registros":len(linhas)})
    manifesto={"particoes":len(grupos),"registros":sum(len(x) for x in grupos.values()),"arquivos":arquivos}; saida.mkdir(parents=True,exist_ok=True); (saida/"manifest.json").write_text(json.dumps(manifesto,indent=2)+"\n",encoding="utf-8"); return manifesto
def main():
    p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/input/eventos.csv"));p.add_argument("--output",type=Path,default=Path("data/output"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
