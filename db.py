import sqlite3
from datetime import datetime

DB_PATH = "documents.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_type    TEXT NOT NULL,
            requirements TEXT NOT NULL,
            content     TEXT NOT NULL,
            created_at  TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_document(doc_type: str, requirements: str, content: str) -> int:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute(
        "INSERT INTO documents (doc_type, requirements, content, created_at) VALUES (?,?,?,?)",
        (doc_type, requirements, content, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    doc_id = cur.lastrowid
    conn.commit()
    conn.close()
    return doc_id

def get_history(limit: int = 10) -> list[dict]:
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT id, doc_type, requirements, content, created_at FROM documents ORDER BY id DESC LIMIT ?",
        (limit,)
    ).fetchall()
    conn.close()
    return [
        {"id": r[0], "doc_type": r[1], "requirements": r[2], "content": r[3], "created_at": r[4]}
        for r in rows
    ]

def delete_document(doc_id: int):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
    conn.commit()
    conn.close()

# Auto-initialize on import
init_db()