# Description: This file contains the database operations for the incidents database.
import sqlite3
from sqlite3 import Connection

DATABASE = "incidents.db"

def get_connection() -> Connection:
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            incident_time TEXT,
            latitude REAL,
            longitude REAL,
            status TEXT DEFAULT 'active'
        )
    ''')
    conn.commit()
    conn.close()

def add_incident(title: str, description: str, incident_time: str, latitude: float, longitude: float, status: str = 'active'):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO incidents (title, description, incident_time, latitude, longitude, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, description, incident_time, latitude, longitude, status))
    conn.commit()
    conn.close()

def get_all_incidents():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents ORDER BY incident_time DESC")
    incidents = cursor.fetchall()
    conn.close()
    return incidents