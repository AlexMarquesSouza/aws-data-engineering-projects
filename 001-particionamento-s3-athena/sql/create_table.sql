CREATE EXTERNAL TABLE IF NOT EXISTS eventos (
  evento_id string,
  ocorrido_em string,
  tipo string,
  usuario_id string
)
PARTITIONED BY (`year` string, `month` string, `day` string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
LOCATION 's3://SEU_BUCKET/eventos/';

MSCK REPAIR TABLE eventos;

SELECT tipo, count(*) AS quantidade
FROM eventos
WHERE year = '2026' AND month = '08' AND day = '04'
GROUP BY tipo;
