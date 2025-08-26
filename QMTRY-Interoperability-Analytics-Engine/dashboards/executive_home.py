import duckdb, streamlit as st, pathlib

st.set_page_config(page_title="QMTRY Executive Home", layout="wide")
st.title("QMTRY — Executive Command Center")
st.caption("Interoperability Without the Drama • Reduce Errors • Improve Timeliness • Unlock Insight")

BASE = pathlib.Path(__file__).resolve().parents[1]
db = duckdb.connect(str(BASE / "warehouse" / "qmtry.duckdb"))

members = db.execute("select count(*) as n from patients").df().iloc[0]["n"]
admin = db.execute("select count(*) as n from meds").df().iloc[0]["n"]
errors = db.execute("select sum(case when administered=0 then 1 else 0 end) as e from meds").df().iloc[0]["e"]
maer = round((errors / admin) * 100, 2) if admin else 0.0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Members", f"{members:,}")
c2.metric("Administrations", f"{admin:,}")
c3.metric("Admin Errors", f"{int(errors):,}")
c4.metric("MAER (%)", f"{maer}%")

st.subheader("Medication Administration Trend")
trend = db.execute("""
  select date_trunc('day', start_time) as day,
         sum(1) as administrations,
         sum(case when administered=0 then 1 else 0 end) as errors
  from meds
  group by 1 order by 1
""").df()
st.line_chart(trend.set_index("day"))

st.subheader("Stars/HEDIS Snapshot")
try:
    stars = db.execute("select * from marts.stars_kpis").df()
    st.table(stars)
except Exception as e:
    st.info("Run dbt build to create marts.stars_kpis (see README).")
