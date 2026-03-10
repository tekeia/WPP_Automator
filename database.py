import sqlite3

DB_FILE = "agenda.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT DEFAULT '09:00',
            message TEXT NOT NULL,
            sent INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_message(phone, date, message, time="09:00"):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO messages (phone, date, time, message) VALUES (?, ?, ?, ?)",
              (phone, date, time, message))
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    rows = c.fetchall()
    conn.close()
    return rows

def get_due_messages(today, current_time):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM messages WHERE date=? AND time=? AND sent=0", (today, current_time))
    rows = c.fetchall()
    conn.close()
    return rows

def mark_sent(message_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE messages SET sent=1 WHERE id=?", (message_id,))
    conn.commit()
    conn.close()