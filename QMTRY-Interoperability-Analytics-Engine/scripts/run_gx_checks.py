import pathlib, duckdb, json, datetime
from great_expectations.dataset import PandasDataset

BASE = pathlib.Path(__file__).resolve().parents[1]
WH = BASE / "warehouse"
EVID = BASE / "evidence"
DOCS = EVID / "data_docs"
EVID.mkdir(exist_ok=True)
DOCS.mkdir(parents=True, exist_ok=True)

db = duckdb.connect(str(WH / "qmtry.duckdb"))
patients = db.execute("select * from patients").df()
meds = db.execute("select * from meds").df()
db.close()

class PatientsDS(PandasDataset): pass
class MedsDS(PandasDataset): pass

pds = PatientsDS(patients)
pds.expect_column_values_to_not_be_null("patient_id")
pds.expect_column_values_to_not_be_null("dob")

mds = MedsDS(meds)
mds.expect_column_values_to_be_in_set("administered", [0,1])
mds.expect_column_values_to_not_be_null("patient_id")

results = {
    "patients": pds.validate().to_json_dict(),
    "meds": mds.validate().to_json_dict(),
}

# minimal html
index = DOCS / "index.html"
ts = datetime.datetime.utcnow().isoformat() + "Z"
html = f"""<!doctype html><html><head><meta charset='utf-8'>
<title>QMTRY Data Docs</title>
<style>body{{font-family:system-ui;-apple-system,Segoe UI,Roboto,sans-serif;background:#0f172a;color:#e5e7eb}}
.card{{background:#111827;padding:16px;margin:16px;border-radius:12px}}
pre{{white-space:pre-wrap;word-break:break-word}}</style></head><body>
<h1>QMTRY Data Quality — Evidence</h1><p>Generated: {ts}</p>
<div class="card"><h2>patients</h2><pre>{json.dumps(results["patients"], indent=2)[:120000]}</pre></div>
<div class="card"><h2>meds</h2><pre>{json.dumps(results["meds"], indent=2)[:120000]}</pre></div>
</body></html>"""
index.write_text(html)
print("Data Docs:", index)
