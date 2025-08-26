with meds as (
  select * from {{ ref('meds_clean') }}
)
select
  count(*) as administrations,
  sum(case when administered = 0 then 1 else 0 end) as admin_errors
from meds
