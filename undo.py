import sqlite3
import shutil
import os

DB_PATH = "database/history.db"

RESTORED_FOLDER = "restored"


def undo_last():

    os.makedirs(
        RESTORED_FOLDER,
        exist_ok=True
    )

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        final_path
    FROM history
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    if row is None:

        print("Nothing to undo.")

        conn.close()

        return

    record_id = row[0]

    final_path = row[1]

    filename = os.path.basename(
        final_path
    )

    restored_path = os.path.join(
        RESTORED_FOLDER,
        filename
    )

    shutil.move(
        final_path,
        restored_path
    )

    cursor.execute(
        """
        DELETE FROM history
        WHERE id=?
        """,
        (record_id,)
    )

    conn.commit()

    conn.close()

    print(
        f"Restored -> {restored_path}"
    )