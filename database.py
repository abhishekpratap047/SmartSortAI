import sqlite3
from datetime import datetime

DB_PATH = "database/history.db"


def initialize_db():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        original_path TEXT,

        renamed_path TEXT,

        final_path TEXT,

        timestamp TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_history(
    original_path,
    renamed_path,
    final_path
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute(
        """
        INSERT INTO history(
            original_path,
            renamed_path,
            final_path,
            timestamp
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            original_path,
            renamed_path,
            final_path,
            timestamp
        )
    )

    conn.commit()
    conn.close()