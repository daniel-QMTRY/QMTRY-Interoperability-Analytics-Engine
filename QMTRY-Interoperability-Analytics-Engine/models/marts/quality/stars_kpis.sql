with base as (
  select * from {{ ref('patients_clean') }}
)
select
  count(*) as member_count,
  sum(case when extract('year' from age(current_date(), dob)) >= 65 then 1 else 0 end) as medicare_like_count
from base
