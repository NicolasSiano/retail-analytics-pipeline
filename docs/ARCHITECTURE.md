# Architecture

## Proposed flow (not implemented in Sprint 0)

```text
Synthetic generator -> CSV/XLSX raw files -> extraction -> validation -> transformation
                                                            |               |
                                                       rejected rows        v
                                                                     SQL Server load
                                                                            |
                                                                   analytical queries
                                                                            |
                                                                  CSV/XLSX / Power BI
```

## Repository layout

```text
src/retail_analytics/
  generation/       Seeded synthetic inputs
  extraction/       CSV and XLSX readers
  validation/       Data contract and rejection reasons
  transformation/   Business rules and normalization
  loading/          SQLAlchemy transactions and idempotency
  reporting/        KPI queries and exports
  orchestration/    Run sequencing and status
  config/           Environment configuration
tests/
  unit/             Isolated behavior tests
  integration/      Explicit SQL Server checks (future)
data/
  raw/              Immutable generated inputs (ignored)
  processed/        Intermediate outputs (ignored)
  rejected/         Quarantined records (ignored)
reports/            Generated exports (ignored)
logs/               Local execution logs (ignored)
sql/                Future versioned SQL scripts; no DDL yet
docs/               Requirements, architecture, roadmap, validation
```

Directories contain placeholders until their sprint begins. Only the root package exists.
The src layout ensures tests exercise the installed package rather than accidentally
importing application code from the repository root.

## Design decisions

- A modular Python batch application is sufficient for 10,000 sales. Avoid distributed
  infrastructure until a demonstrated requirement justifies it.
- Pandas handles tabular operations; openpyxl supplies XLSX reading and writing.
- SQLAlchemy provides connection and transaction management over pyodbc. A compatible
  Microsoft ODBC driver is a separate operating-system prerequisite, not a pip package.
- Prefer Windows integrated authentication locally where available. Never embed credentials.
- Standard-library logging, pathlib, decimal, and random avoid unnecessary dependencies.
- Proposed database layers: staging, curated sales/dimensions, and analytical views.
  Grain, schema, and SQL objects will be designed in the database sprint.
- Idempotency must combine stable business keys, database uniqueness, and transactional
  loading. Pandas deduplication alone cannot protect against reruns or partial failures.
- Audit metadata should include run ID, source file, row counts, rejected counts, timing,
  and status. Define reconciliation across duplicate and invalid records before implementation.
- Keep monetary values exact at persistence boundaries; agree on rounding before KPIs.
- Runtime dependencies have bounded ranges in pyproject.toml. requirements-dev.lock.txt
  records the tested Windows/Python 3.13 environment including transitive dependencies.
  It is a pip freeze snapshot, not a cross-platform or hash-verified lock.

## References

- [Pandas distribution](https://pypi.org/project/pandas/)
- [pyodbc distribution](https://pypi.org/project/pyodbc/)
- [SQLAlchemy SQL Server dialect](https://docs.sqlalchemy.org/en/20/dialects/mssql.html)
