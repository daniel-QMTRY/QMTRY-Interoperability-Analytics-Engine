with src as (
  select * from read_csv_auto('data/bronze/patients.csv')
)
select
  cast(patient_id as varchar) as patient_id,
  coalesce(first_name,'') as first_name,
  coalesce(last_name,'') as last_name,
  cast(dob as date) as dob,
  gender,
  coalesce(mrn,'') as mrn
from src
