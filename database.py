
import sqlite3
from datetime import datetime

DB_NAME = "portfolio.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS portfolio (
        symbol TEXT PRIMARY KEY,
        amount REAL NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        action TEXT,
        symbol TEXT,
        amount REAL
    )
    """)

    conn.commit()
    conn.close()


def add_asset(symbol, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO portfolio(symbol, amount)
    VALUES (?, ?)
    ON CONFLICT(symbol)
    DO UPDATE SET amount = amount + excluded.amount
    """, (symbol.upper(), amount))

    cur.execute("""
    INSERT INTO transactions(date, action, symbol, amount)
    VALUES (?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        "ADD",
        symbol.upper(),
        amount
    ))

    conn.commit()
    conn.close()


def remove_asset(symbol, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    UPDATE portfolio
    SET amount = amount - ?
    WHERE symbol = ?
    """, (amount, symbol.upper()))

    cur.execute("""
    INSERT INTO transactions(date, action, symbol, amount)
    VALUES (?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        "SELL",
        symbol.upper(),
        amount
    ))

    conn.commit()
    conn.close()


def get_portfolio():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT symbol, amount FROM portfolio
    """)

    data = cur.fetchall()
    conn.close()

    return data
