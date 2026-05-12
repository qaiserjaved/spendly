import sqlite3
import os
from werkzeug.security import generate_password_hash

DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "spendly.db")


def get_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    try:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            );
        
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)
        conn.commit()
    finally:
        conn.close()


def seed_db():
    conn = get_db()
    try:
        existing = conn.execute("SELECT COUNT(*) as count FROM users").fetchone()
        if existing[0] > 0:
            conn.close()
            return

        password_hash = generate_password_hash("demo123")
        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", password_hash)
        )
        user_id = cursor.lastrowid

        expenses = [
            (user_id, 15.50, "Food", "2026-05-02", "Lunch at cafe"),
            (user_id, 45.00, "Transport", "2026-05-03", "Uber ride"),
            (user_id, 120.00, "Bills", "2026-05-05", "Electricity bill"),
            (user_id, 25.00, "Health", "2026-05-07", "Pharmacy"),
            (user_id, 35.00, "Entertainment", "2026-05-09", "Movie tickets"),
            (user_id, 89.99, "Shopping", "2026-05-11", "New headphones"),
            (user_id, 12.00, "Other", "2026-05-12", "Coffee"),
            (user_id, 50.00, "Food", "2026-05-13", "Grocery shopping"),
        ]

        for expense in expenses:
            conn.execute(
                "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
                expense
            )

        conn.commit()
    finally:
        conn.close()