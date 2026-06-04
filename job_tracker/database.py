import sqlite3

def init_db():
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id integer primary key autoincrement,
            role text not null,
            company text not null, 
            application_date text,
            status text not null default 'Applied',
            note text default null
        )
        """)


