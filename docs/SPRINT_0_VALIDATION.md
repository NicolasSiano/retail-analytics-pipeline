# Sprint 0 validation

Validated on 2026-10-15 (America/Montevideo), Windows, Python 3.13.16.

## Baseline

- Repository origin: https://github.com/NicolasSiano/retail-analytics-pipeline.git
- Initially present: README.md, LICENSE, and a generic Python .gitignore.
- Initial working tree was clean; no existing AGENTS.md or Python application found.
- `python` resolved to Python 3.13.16; `py -0p` reported no installed Pythons.

## Results

| Check | Result |
| --- | --- |
| Local .venv creation and interpreter | Passed, Python 3.13.16 |
| Editable installation with development dependencies | Passed |
| pytest | 3 passed |
| pip check | No broken requirements found |
| Ruff lint and format | Passed |
| git diff --check | Passed |
| Ignore probes | .venv, .env, .env.production, credentials, temporary files, raw data, and reports ignored |
| ODBC discovery | Microsoft ODBC Driver 17 and 18 for SQL Server present |

Tests exercise installed package/configuration imports, CSV and XLSX round trips in
memory, and SQLAlchemy's pyodbc dialect initialization without a database connection.
They do not generate retail sales or implement ETL transformations.

## Installed direct dependencies

| Package | Version |
| --- | --- |
| pandas | 3.0.6 |
| openpyxl | 3.1.5 |
| SQLAlchemy | 2.0.54 |
| pyodbc | 5.3.0 |
| python-dotenv | 1.2.4 |
| pytest | 9.1.1 |
| ruff | 0.17.1 |
| setuptools | 82.0.1 |

The full installed dependency snapshot is in requirements-dev.lock.txt, excluding
the editable application. Build tools are included for offline editable installation
after dependencies are installed. Package downloads initially failed under restricted
network access; the authorized retry completed successfully. Installation caches and
temporary paths were directed inside the repository.

## Boundaries

No database connection, DDL, generator, ETL, commits, or pushes were performed.
SQL Server version, RetailAnalyticsDB existence/content, authentication, and permissions
remain user-reported or unverified. Sprint 1 requires explicit approval.
