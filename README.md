# Radar de Engenharia de Dados · AWS

| # | Projeto | Conceitos | Status |
|---:|---|---|---|
| 000 | [Configuração do ambiente](000-configuracao-ambiente/README.md) | VS Code, Python, Git, AWS CLI opcional | Rascunho para revisão |
| 001 | [Particionamento para S3 e Athena](001-particionamento-s3-athena/README.md) | S3, Athena, prefixos Hive | Rascunho para revisão |
| 002 | [Detector de schema drift](002-detector-schema-drift-glue/README.md) | Glue Crawler, contratos, catálogo | Rascunho para revisão |
| 003 | [Job bookmark incremental](003-job-bookmark-glue/README.md) | Glue ETL, bookmark, idempotência | Rascunho para revisão |
| 004 | [Retentativas e DLQ no SQS](004-sqs-retry-dlq/README.md) | SQS, redrive, resiliência | Rascunho para revisão |
| 005 | [Step Functions com Retry e Catch](005-step-functions-retry-catch/README.md) | Orquestração, backoff, fallback | Rascunho para revisão |
| 006 | [Advisor de desenho físico Redshift](006-redshift-table-design-advisor/README.md) | Redshift, distkey, sortkey | Rascunho para revisão |
| 007 | [Detector de hot keys DynamoDB](007-dynamodb-hot-key-detector/README.md) | DynamoDB, RCU, distribuição | Rascunho para revisão |
| 008 | [Planejador de shards Kinesis](008-kinesis-shard-planner/README.md) | Kinesis, shards, throughput | Rascunho para revisão |
| 009 | [Qualidade com Glue DQDL](009-glue-data-quality-dqdl/README.md) | Glue Data Quality, DQDL, score | Rascunho para revisão |
| 010 | [Auditor de permissões Lake Formation](010-lake-formation-permission-auditor/README.md) | Lake Formation, colunas, menor privilégio | Rascunho para revisão |
| 011 | [Compatibilidade de schemas Glue](011-glue-schema-compatibility-checker/README.md) | Glue Schema Registry, Avro, contratos | Rascunho para revisão |
| 012 | [Auditor IAM para jobs Glue](012-glue-job-iam-policy-auditor/README.md) | Glue, IAM, menor privilégio | Rascunho para revisão |
| 013 | [Advisor de workers Glue](013-glue-worker-sizing-advisor/README.md) | Glue, workers, DPU, right-sizing | Rascunho para revisão |

Nenhum projeto pode ser publicado ou implantado sem aprovação manual.


## Manutenção deste repositório

Este diretório é autônomo: contém documentação, dependências do site, testes estruturais e scripts próprios. Após clonar:

```bash
cd "caminho/para/aws-data-engineering-projects"
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-docs.txt
python3 scripts/validate_projects.py
bash scripts/build_site.sh
```

O build gera somente documentação local. Publicação, criação de repositório remoto e `git push` continuam manuais.
