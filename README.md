# Retail Analytics Pipeline

A data engineering and BI portfolio using **100% synthetic data**, Python, Pandas,
SQL Server, and eventually Power BI. Target: approximately 10,000 sales across three
branches and 12 consecutive months.

**Status: Sprint 0 foundation.** No generator, ETL transformations, SQL tables, or dashboard yet.

## Setup (Windows PowerShell)

Run from the repository root with Python 3.13 (validated with 3.13.16).
Use `python`; the local `py` launcher did not discover its installation.

```powershell
python --version
python -m venv .venv
New-Item -ItemType Directory -Force .tmp | Out-Null
$env:TEMP = Join-Path (Get-Location) '.tmp'
$env:TMP = $env:TEMP
$env:PIP_CACHE_DIR = Join-Path (Get-Location) '.tmp/pip-cache'
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.lock.txt
.\.venv\Scripts\python.exe -m pip install --no-build-isolation --no-deps -e .
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
```

Optional activation: `.\.venv\Scripts\Activate.ps1`; leave with `deactivate`.
If activation is blocked, use the direct interpreter commands above; no policy changes
are necessary. Select `.venv\Scripts\python.exe` as the VS Code interpreter.

To intentionally resolve fresh versions within pyproject.toml ranges, run
`.\.venv\Scripts\python.exe -m pip install -e ".[dev]"`.
Review and retest updates before refreshing the version snapshot. The snapshot excludes
the editable project, which is installed separately; it is not a cross-platform lock.

## Dependencies

| Dependency | Purpose |
| --- | --- |
| pandas | Tabular processing and analysis |
| openpyxl | XLSX reading and writing |
| SQLAlchemy | SQL connections, transactions, and SQL Server dialect |
| pyodbc | Python ODBC interface |
| python-dotenv | Future local environment configuration |
| pytest (dev) | Automated tests |
| Ruff (dev) | Lint and formatting |
| setuptools (build) | Installable src-layout package |

Standard-library logging, pathlib, random, and decimal will cover common utilities.

## SQL Server

SQL Server 2025 Developer and RetailAnalyticsDB are user-reported existing resources.
A Microsoft ODBC driver is a separate operating-system prerequisite, not a pip package.
Inspect installed drivers without connecting:

```powershell
.\.venv\Scripts\python.exe -c "import pyodbc; print(pyodbc.drivers())"
```

Sprint 0 does not verify server connectivity, authentication, permissions, or database
contents, and does not create SQL objects. Database checks belong to Sprint 3.
Never commit secrets; future local configuration must remain ignored.

## Design and documentation

Planned flow: synthetic CSV/XLSX -> extraction -> validation/quarantine -> transformation
-> transactional SQL Server loading -> KPIs -> CSV/XLSX reports and Power BI.

- [Requirements](docs/REQUIREMENTS.md)
- [Architecture and directory responsibilities](docs/ARCHITECTURE.md)
- [Roadmap and exercises for each task](docs/ROADMAP.md)
- [Sprint 0 validation](docs/SPRINT_0_VALIDATION.md)
- [Learning rules](AGENTS.md)

Generated data, reports, logs, secrets, caches, and .venv are ignored; output folders
retain tracked placeholders. Smoke tests cover imports/configuration, in-memory CSV/XLSX
round trips, and offline SQL dialect initialization, not ETL or database correctness.

Next: approve Sprint 1, then agree on the sales data contract before generation.
No commits or pushes without explicit authorization.

## License

See [LICENSE](LICENSE).
