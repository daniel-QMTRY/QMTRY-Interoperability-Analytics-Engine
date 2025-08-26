with src as (
  select * from read_csv_auto('data/bronze/meds.csv')
)
select
  cast(patient_id as varchar) as patient_id,
  med_code,
  med_name,
  route,
  cast(start_time as timestamp) as start_time,
  cast(end_time as timestamp) as end_time,
  administered as administered
from src
