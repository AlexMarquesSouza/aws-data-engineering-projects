import argparse,json,math
from pathlib import Path
WORKERS={"G.1X":{"dpu":1,"memory_gb":16},"G.2X":{"dpu":2,"memory_gb":32},"G.4X":{"dpu":4,"memory_gb":64},"R.1X":{"dpu":1,"memory_gb":32}}
def recommend(job):
    worker="R.1X" if job.get("memory_bound") else ("G.4X" if job["input_gb"]>=500 else "G.2X" if job["input_gb"]>=100 else "G.1X")
    workers=max(2,math.ceil(job["input_gb"]/(50*WORKERS[worker]["dpu"])))
    return {"job":job["name"],"worker_type":worker,"number_of_workers":workers,"total_dpu":workers*WORKERS[worker]["dpu"],"reason":"memory-optimized" if job.get("memory_bound") else "general-purpose por volume"}
def advise(jobs): return {"recommendations":[recommend(x) for x in jobs]}
def main():
    p=argparse.ArgumentParser(); p.add_argument("input",nargs="?",default="data/jobs.json"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args(); report=advise(json.loads(Path(a.input).read_text())["jobs"]); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n"); print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
