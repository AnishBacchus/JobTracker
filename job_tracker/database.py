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

def add_application(role, company, application_date, status, note):
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO applications (role, company, application_date, status, note) 
                       values (?, ?, ?, ?, ?)
                    """, (role, company, application_date, status, note))
        


def get_applications():
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM applications")
        jobs_applied = cursor.fetchall()
        return jobs_applied