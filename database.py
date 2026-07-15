import sqlite3
import hashlib
import re
import random
from datetime import datetime

DB_NAME = "scan_system.db"


# ======================
# CONNECTION (SAFE)
# ======================
def get_connection():
    conn = sqlite3.connect(DB_NAME, timeout=10)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


# ======================
# HASH PASSWORD
# ======================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def is_valid_password(password):

    if len(password) < 12:
        return "Password must be at least 12 characters"

   
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter"

    
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter"

    
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number"

    
    if not re.search(r'[@$!%*?&#+_=.-]', password):
        return "Password must contain at least one special character"

    return True
# ======================
# URL VALIDATION
# ======================
def is_valid_url(text):
    pattern = re.compile(r'^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}')
    return bool(pattern.match(text))
# ======================
# TIME AGO
# ======================
def time_ago(time_str):
    past = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()

    diff = now - past
    seconds = diff.total_seconds()

    if seconds < 3600:
        return f"{int(seconds // 60)} minutes ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours ago"
    else:
        return f"{int(seconds // 86400)} days ago"
# CREATE TABLES
# ======================
def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            content TEXT NOT NULL,
            type TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            report_id INTEGER,
            score INTEGER,
            risk_level TEXT,
            reason TEXT,
            scan_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE recent_threat_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            content TEXT,
            type TEXT,
            risk_level TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE recent_threat_detected (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            risk_level TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE early_warning_alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            type TEXT,
            risk_level TEXT,
            total_reports INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE statistics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scans_completed INTEGER DEFAULT 0,
            threats_blocked INTEGER DEFAULT 0,
            active_users INTEGER DEFAULT 0,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE password_resets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            code TEXT,
            used INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        print("Database ready ")


# ======================
# ADD SCAN
# ======================
def add_scan(user_id, username, score, risk_level,
             reason, content, report_type):
    conn = sqlite3.connect(DB_NAME, timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")
    cursor = conn.cursor()

    try:
        # scans table (auto id)
        cursor.execute("""
INSERT INTO scans (score, risk_level, reason)
VALUES (?, ?, ?)
""", (score, risk_level, reason))
        # activity table
        cursor.execute("""
INSERT INTO recent_threat_activity
(user_id, username, content, type, risk_level)
VALUES (?, ?, ?, ?, ?)
""", (
    user_id,
    username,
    content,
    report_type,
    risk_level
))
        cursor.execute("""
INSERT INTO recent_threat_detected (content, risk_level)
VALUES (?, ?)
""", (content, risk_level))

        if risk_level.lower() == "high":

         # نشوف كم مرة تكرر نفس المحتوى
          cursor.execute("""
SELECT COUNT(*)
FROM recent_threat_activity
WHERE content = ?
""", (content,))

          count = cursor.fetchone()[0]

          if count >= 2:

    # هل موجود من قبل بالalerts؟
              cursor.execute("""
    SELECT id, total_reports
    FROM early_warning_alerts
    WHERE content = ?
    """, (content,))

              existing = cursor.fetchone()

    # اذا مش موجود ضيفه
              if not existing:

               cursor.execute("""
        INSERT INTO early_warning_alerts
        (content, type, risk_level, total_reports)
        VALUES (?, ?, ?, ?)
        """, (content, report_type, risk_level, count))

              else:
        # اذا موجود حدث عدد البلاغات
                 cursor.execute("""
        UPDATE early_warning_alerts
        SET total_reports = ?
        WHERE id = ?
        """, (count, existing[0]))
        conn.commit()
    finally:
        conn.close()
# SIGN UP
def signup(username, email, password):

    validation = is_valid_password(password)

    if validation != True:
        return validation

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            return "User already exists"

        cursor.execute("""
        INSERT INTO users (username, email, password_hash)
        VALUES (?, ?, ?)
        """, (username, email, hash_password(password)))

        conn.commit()
        return "User created successfully"
# LOGIN
# ======================
def login(email, password):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, username, password_hash
        FROM users
        WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if not user:
            return "Email is incorrect"

        user_id, username, stored_password = user

        if stored_password != hash_password(password):
            return "Password is incorrect"

        return {
            "message": "Login successful",
            "user_id": user_id,
            "username": username
        }
# ======================
# ADD REPORT
# ======================
def add_report(user_id, content, report_type):

    if report_type == "url":
        if not is_valid_url(content):
            return "Invalid URL"

    if report_type == "message":
        if content.strip() == "":
            return "Empty message"

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO reports (user_id, content, type)
        VALUES (?, ?, ?)
        """, (user_id, content, report_type))

        conn.commit()
        return cursor.lastrowid
def get_recent_threats_detected():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT content, risk_level
        FROM recent_threat_detected
        ORDER BY id DESC
        LIMIT 3
        """)

        rows = cursor.fetchall()

        threats = []

        for row in rows:
            threats.append({
                "content": row[0],
                "risk_level": row[1]
            })

        return threats
def scans_completed():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        """)

        return cursor.fetchone()[0]
def threats_blocked():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        WHERE LOWER(risk_level) LIKE '%high%'
        """)

        return cursor.fetchone()[0]

        return cursor.fetchone()[0]

def active_users():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM users
        """)

        return cursor.fetchone()[0]
def get_recent_threats_activity():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT type, content, risk_level, created_at
        FROM recent_threat_activity
        ORDER BY created_at DESC
        LIMIT 5
        """)

        rows = cursor.fetchall()

        activities = []

        for row in rows:
            activities.append({
                "type": row[0],
                "content": row[1],
                "risk_level": row[2],
                "time_ago": row[3]
            })

        return activities
        return cursor.fetchall()
def get_high_alerts():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT type, content, risk_level, total_reports
        FROM early_warning_alerts
        ORDER BY created_at DESC
        LIMIT 3
        """)

        rows = cursor.fetchall()

        alerts = []

        for row in rows:
            alerts.append({
                "type": row[0],
                "content": row[1],
                "risk_level": row[2],
                "total_reports": row[3]
            })

        return alerts

def save_early_warning(alert_type, content, risk_level):

    with get_connection() as conn:
        cursor = conn.cursor()

        # عدّ كم مرة نفس المحتوى انفحص
        cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        WHERE reason = ?
        """, (content,))

        count = cursor.fetchone()[0]

        # فقط اذا تكرر مرتين او اكثر
        if count >= 2:

            # هل موجود مسبقاً؟
            cursor.execute("""
            SELECT id, total_reports
            FROM early_warning_alerts
            WHERE content = ?
            """, (content,))

            existing = cursor.fetchone()

            # اذا مش موجود ضيفه
            if not existing:

                cursor.execute("""
                INSERT INTO early_warning_alerts
                (type, content, risk_level, total_reports)
                VALUES (?, ?, ?, ?)
                """, (alert_type, content, risk_level, count))

            else:
                # اذا موجود حدث عدد البلاغات
                cursor.execute("""
                UPDATE early_warning_alerts
                SET total_reports = ?
                WHERE content = ?
                """, (count, content))

            conn.commit()
def add_user(username, email, password_hash):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO users (username, email, password_hash)
        VALUES (?, ?, ?)
        """, (username, email, password_hash))

        conn.commit()
def get_user(username):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM users
        WHERE username = ?
        """, (username,))

        return cursor.fetchone()
def save_reset_code(user_id, code):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO password_resets (user_id, code)
        VALUES (?, ?)
        """, (user_id, code))

        conn.commit()
def get_reset_code(code):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM password_resets
        WHERE code = ? AND used = 0
        """, (code,))

        return cursor.fetchone()

def update_password(user_id, password_hash):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE users
        SET password_hash = ?
        WHERE id = ?
        """, (password_hash, user_id))

        conn.commit()
def mark_code_used(code):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE password_resets
        SET used = 1
        WHERE code = ?
        """, (code,))

        conn.commit()