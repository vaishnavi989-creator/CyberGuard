from fastapi import FastAPI
import sqlite3

from backend.url_analyzer import analyze_url
from backend.risk_engine import calculate_risk


app = FastAPI()


# Database table create karna
def create_database():

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


# App start hote hi database create hoga
create_database()


@app.get("/")
def home():
    return {"message": "CyberGuard API is running!"}


@app.get("/scan")
def scan_url(url: str):

    features = analyze_url(url)

    risk_score, result, risk_level, reasons = calculate_risk(features)

    connection = sqlite3.connect("cyberguard.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO scans
        (url, risk_score, result, risk_level, reasons)
        VALUES (?, ?, ?, ?, ?)
    """, (
        url,
        risk_score,
        result,
        risk_level,
        str(reasons)
    ))

    connection.commit()
    connection.close()

    return {
        "url": url,
        "risk_score": risk_score,
        "result": result,
        "risk_level": risk_level,
        "reasons": reasons
    }


@app.get("/history")
def scan_history():

    connection = sqlite3.connect("cyberguard.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, url, risk_score, result, risk_level, reasons, scan_time
        FROM scans
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    history = []

    for row in rows:
        history.append({
            "id": row[0],
            "url": row[1],
            "risk_score": row[2],
            "result": row[3],
            "risk_level": row[4],
            "reasons": row[5],
            "scan_time": row[6]
        })

    return history