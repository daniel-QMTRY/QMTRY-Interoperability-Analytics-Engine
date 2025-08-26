import pathlib, datetime, zipfile

BASE = pathlib.Path(__file__).resolve().parents[1]
EVID = BASE / "evidence"
TARGET = BASE / "target"
bundle = EVID / f"evidence_bundle_{datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.zip"
bundle.parent.mkdir(exist_ok=True)

with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
    for folder in [EVID / "data_docs", TARGET]:
        if folder.exists():
            for p in folder.rglob("*"):
                if p.is_file():
                    z.write(p, p.relative_to(BASE))
    (EVID / "SUMMARY.md").write_text("# Evidence Bundle\n\nIncludes data docs and dbt artifacts.")
    z.write(EVID / "SUMMARY.md", "evidence/SUMMARY.md")

print("Evidence bundle:", bundle)
