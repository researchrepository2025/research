# schema.py - SQLite DDL and DB creation
import sqlite3
from pathlib import Path

DB_DIR = Path(__file__).parent.parent / "db"


def create_schema(conn):
    """Create all tables."""
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS scopes (
            scope_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        INSERT OR IGNORE INTO scopes VALUES (1, 'global'), (2, 'europe_canada');

        CREATE TABLE IF NOT EXISTS companies (
            company_id INTEGER PRIMARY KEY AUTOINCREMENT,
            canonical_name TEXT NOT NULL UNIQUE,
            parent_company TEXT,
            hq_location TEXT,
            known_total_revenue_usd_m REAL
        );

        CREATE TABLE IF NOT EXISTS segments (
            segment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            segment_number INTEGER NOT NULL,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            market_size_usd_m REAL,
            scope_id INTEGER NOT NULL REFERENCES scopes(scope_id),
            UNIQUE(segment_number, scope_id)
        );

        CREATE TABLE IF NOT EXISTS company_segments (
            cs_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER NOT NULL REFERENCES companies(company_id),
            segment_id INTEGER NOT NULL REFERENCES segments(segment_id),
            rank INTEGER,
            revenue_usd_m REAL,
            revenue_label TEXT,
            market_share_pct REAL,
            estimated_share_pct REAL,
            share_confidence TEXT,
            key_metric_raw TEXT,
            source_url TEXT,
            UNIQUE(company_id, segment_id)
        );
    """)


def create_db(db_path=None):
    """Create database file and schema, return connection."""
    if db_path is None:
        DB_DIR.mkdir(parents=True, exist_ok=True)
        db_path = DB_DIR / "market_leaders.db"
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")
    create_schema(conn)
    conn.commit()
    return conn
