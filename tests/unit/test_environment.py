"""Offline capability checks; no sales data generation or database connections."""

from io import BytesIO, StringIO

import pandas as pd
import pyodbc
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

import retail_analytics


def test_installed_package_and_configuration():
    assert retail_analytics.__doc__
    assert dotenv_values(stream=StringIO("APP_MODE=test\n")) == {"APP_MODE": "test"}


def test_tabular_io_round_trip():
    expected = pd.DataFrame({"value": [1, 2], "label": ["alpha", "beta"]})
    csv_buffer = StringIO()
    expected.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    pd.testing.assert_frame_equal(pd.read_csv(csv_buffer), expected)
    excel_buffer = BytesIO()
    expected.to_excel(excel_buffer, index=False, engine="openpyxl")
    excel_buffer.seek(0)
    pd.testing.assert_frame_equal(pd.read_excel(excel_buffer, engine="openpyxl"), expected)


def test_sql_server_dialect_without_connection():
    url = URL.create(
        "mssql+pyodbc",
        host="localhost",
        database="RetailAnalyticsDB",
        query={"driver": "ODBC Driver 18 for SQL Server"},
    )
    engine = create_engine(url)
    assert engine.dialect.name == "mssql"
    assert engine.dialect.dbapi is pyodbc
    engine.dispose()
