import sqlite3

connection = sqlite3.connect("cyberguard.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    risk_score INTEGER,
    result TEXT,
    risk_level TEXT,
    reasons TEXT,
    scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
connection.close()

print("Database created successfully!")