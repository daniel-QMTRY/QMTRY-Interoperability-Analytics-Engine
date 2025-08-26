<p align="center">
  <img src="https://img.shields.io/badge/QMTRY-Interoperability_&_Analytics-00B3A4?style=for-the-badge" alt="QMTRY badge"/>
  <img src="https://img.shields.io/badge/HIPAA-Aware-007C78?style=for-the-badge" alt="HIPAA"/>
  <img src="https://img.shields.io/badge/Stars/HEDIS-Ready-00B3A4?style=for-the-badge" alt="HEDIS"/>
  <img src="https://img.shields.io/badge/License-MIT-1D1D1D?style=for-the-badge" alt="MIT"/>
</p>

<h1 align="center">Interoperability Without the Drama</h1>
<h3 align="center">Reduce Errors. Improve Timeliness. Unlock Insight. 🚀</h3>

<p align="center">
  From chaotic HL7/FHIR feeds to <em>audit-ready, executive-grade analytics</em>—built for public trust and federal partners.<br/>
  <a href="../../issues">Report Bug</a> · <a href="../../issues">Request Feature</a>
</p>

---

## Executive Summary

**QMTRY** turns fragmented health data into defensible decisions—fast.
- **Fewer preventable errors** via Data Quality Gates and closed-loop safety patterns.
- **Faster time-to-insight** via CI/CD for analytics and local-first, cloud-ready storage.
- **Evidence on demand** (signed bundles: tests, lineage, SLAs) for auditors and boards.

> This is not a black box. It’s an **auditable system** that reduces risk while accelerating outcomes.

---

## Brand & Procurement Snapshot
- **Palette:** `#1D1D1D` (charcoal) · `#00B3A4` (primary teal) · `#007C78` (hover) · `#FFFFFF` headings · `#F5F5F5` subheads  
- **Positioning:** Federal Health IT subcontractor + PMO partner (minority-owned small business)  
- **SAM.gov UEI:** **G1RAMD6SHKZ1** (active) · **Teaming:** contracts@qmtry.com  
- **PMO page:** `/capability/#subk-pmo`

---

## Why it Works

| Capability | What Leaders Get |
| --- | --- |
| Interoperability without the drama | HL7 v2 + FHIR + claims adapters; normalization (LOINC/RxNorm/SNOMED) you can inspect. |
| Quality by default | Data Quality Gates block “bad data” before it hits executive dashboards. |
| Speed with control | CI/CD for analytics; promote only when tests + freshness + SLAs pass. |
| Clinically relevant | Stars/HEDIS tiles, denials intelligence, early-warning templates. |
| Evidence, not anecdotes | Signed **Evidence Bundle**: test logs, lineage, data docs, timing proof. |

---

## Architecture

```mermaid
flowchart LR
  A[Sources\nHL7 v2 · FHIR · Claims/CSV] --> B[Raw Landing]
  B --> C[Data Quality Gates\n(Great Expectations)]
  C -- pass --> D[Bronze Storage\n(Parquet · DuckDB)]
  C -- fail --> Q[Quarantine + Alert + Data Docs]
  D --> E[dbt Transforms\nCanonical Models]
  E --> G[Gold Marts\nQuality · Finance · Operations]
  G --> H[Executive Dashboards\n(Streamlit)]
  G --> R[Real-time Signals]
  C --> ED[Evidence: Data Docs]
  E --> EL[Evidence: Lineage + Tests]
  G --> ES[Evidence: Signed Bundle (.zip)]
```

### ASCII Fallback

```
[SOURCES: HL7 v2 | FHIR | Claims/CSV]
            |
       [Raw Landing]
            |
      [Data Quality Gates]----fail---->[Quarantine + Alert + Data Docs]
            |
           pass
            v
   [Bronze (Parquet/DuckDB)]
            |
      [dbt Transforms]
            |
       [Gold Marts]
        /         \
[Executive Dashboards]   [Real-time Signals]

Evidence taps:
- From Gates -> Data Docs
- From dbt   -> Lineage + Tests
- From Gold  -> Signed Evidence Bundle (.zip)
```

---

## 5-Minute Demo

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/make_demo_data.py
dbt deps && dbt build --profiles-dir .
python scripts/run_gx_checks.py
streamlit run dashboards/executive_home.py
```

You’ll see **Data Quality Gate** results, Stars/HEDIS tiles, CFO KPIs, and a downloadable **Evidence Bundle**.

---

## KPIs We Move

**Safety & Quality**
- Medication Administration Error Rate (MAER) ↓ — `errors / administrations`
- Sepsis time-to-antibiotics ↓ and in-hospital mortality ↓

**Operations & Finance**
- Time-to-Insight (TTI) ↓ — `data arrival → dashboard publish`
- Denials & avoidable write-offs ↓ — CARC/RARC root-cause drilldowns

**Governance**
- Data Quality Score (DQS) ↑ — completeness, validity, timeliness, consistency

---

## Repo Layout

```
scripts/             # demo data, GX checks, evidence bundle
dashboards/          # Streamlit executive dashboard
models/              # dbt models (duckdb)
  staging/
  marts/quality/
  marts/ops/
evidence/            # generated: data docs, zipped bundles
warehouse/           # duckdb file (local)
assets/              # screenshots (optional)
```

---

## Get Help / Engage
- **Email:** contracts@qmtry.com  
- **Pilot:** 30-Day *Insight Sprint* — wire 2–3 feeds, ship dashboards, deliver evidence.

## License
MIT — see `LICENSE`.
