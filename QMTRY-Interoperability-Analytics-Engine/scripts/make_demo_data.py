import os, random, csv, datetime, duckdb, pathlib
from faker import Faker

fake = Faker()
random.seed(7)

BASE = pathlib.Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "bronze"
WH = BASE / "warehouse"
DATA.mkdir(parents=True, exist_ok=True)
WH.mkdir(parents=True, exist_ok=True)

# Patients
patients_file = DATA / "patients.csv"
with open(patients_file, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["patient_id","first_name","last_name","dob","gender","mrn"])
    for i in range(1,601):
        dob = fake.date_between(start_date="-90y", end_date="-1y")
        w.writerow([i, fake.first_name(), fake.last_name(), dob, random.choice(["M","F"]), f"MRN{i:06d}"])

# Med administrations (simulate 5 per patient, 5% not administered -> 'error')
meds_file = DATA / "meds.csv"
now = datetime.datetime.now()
with open(meds_file, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["patient_id","med_code","med_name","route","start_time","end_time","administered"])
    for pid in range(1,601):
        for _ in range(5):
            start = now - datetime.timedelta(days=random.randint(0,30), hours=random.randint(0,23))
            end = start + datetime.timedelta(minutes=random.randint(5,90))
            admin = 0 if random.random() < 0.05 else 1
            w.writerow([pid,"RX001","Ceftriaxone","IV",start.isoformat(),end.isoformat(),admin])

# Load to DuckDB
con = duckdb.connect(str(WH / "qmtry.duckdb"))
con.execute("CREATE SCHEMA IF NOT EXISTS main;")
con.execute("CREATE OR REPLACE TABLE patients AS SELECT * FROM read_csv_auto(?)", [str(patients_file)])
con.execute("CREATE OR REPLACE TABLE meds AS SELECT * FROM read_csv_auto(?)", [str(meds_file)])
con.close()

print("Demo data created:", patients_file, meds_file)
