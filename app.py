import sqlite3
import pandas as pd
import streamlit as st

from undo import undo_last

DB_PATH = "database/history.db"

st.set_page_config(
    page_title="SmartSort AI",
    layout="wide"
)

st.title("📂 SmartSort AI")

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql_query(
    """
    SELECT *
    FROM history
    ORDER BY id DESC
    """,
    conn
)

conn.close()

st.subheader("Recent Activity")

st.dataframe(df)

st.subheader("Statistics")

if len(df) > 0:

    categories = (
        df["final_path"]
        .str.split("\\\\")
        .str[-2]
        .value_counts()
    )

    st.bar_chart(categories)

else:

    st.info(
        "No files processed yet."
    )

st.subheader("Actions")

if st.button(
    "Undo Last Action"
):

    undo_last()

    st.success(
        "Undo completed."
    )