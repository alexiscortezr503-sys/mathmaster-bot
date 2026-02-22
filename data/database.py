import sqlite3, os
from datetime import datetime, date

DB_PATH = "data/mathmaster.db"

def _conn():
    os.makedirs("data", exist_ok=True)
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    c = _conn()
    c.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        user_id    INTEGER PRIMARY KEY,
        username   TEXT, first_name TEXT,
        xp         INTEGER DEFAULT 0,
        streak     INTEGER DEFAULT 0,
        last_date  TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS exercise_log (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id     INTEGER, topic TEXT,
        correct     INTEGER, hints INTEGER DEFAULT 0,
        ts          TEXT DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS exam_log (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id    INTEGER, level TEXT, topic TEXT,
        score      INTEGER, total INTEGER, pct REAL,
        ts         TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)
    c.commit(); c.close()

def upsert_user(uid, username, first_name):
    c = _conn()
    row = c.execute("SELECT * FROM users WHERE user_id=?", (uid,)).fetchone()
    today = date.today().isoformat()
    if not row:
        c.execute("INSERT INTO users(user_id,username,first_name,last_date) VALUES(?,?,?,?)",
                  (uid, username, first_name, today))
    else:
        # update streak
        streak = row["streak"]
        last   = row["last_date"]
        if last != today:
            from datetime import timedelta
            yesterday = (date.today() - timedelta(days=1)).isoformat()
            streak = (streak + 1) if last == yesterday else 1
        c.execute("UPDATE users SET username=?,first_name=?,last_date=?,streak=? WHERE user_id=?",
                  (username, first_name, today, streak, uid))
    c.commit(); c.close()

def add_xp(uid, amount):
    c = _conn(); c.execute("UPDATE users SET xp=xp+? WHERE user_id=?", (amount, uid))
    c.commit(); c.close()

def get_user(uid):
    c = _conn()
    row = c.execute("SELECT * FROM users WHERE user_id=?", (uid,)).fetchone()
    c.close()
    return dict(row) if row else {}

def log_exercise(uid, topic, correct, hints=0):
    c = _conn()
    c.execute("INSERT INTO exercise_log(user_id,topic,correct,hints) VALUES(?,?,?,?)",
              (uid, topic, int(correct), hints))
    c.commit(); c.close()

def log_exam(uid, level, topic, score, total):
    pct = round(score/total*100, 1) if total else 0
    c = _conn()
    c.execute("INSERT INTO exam_log(user_id,level,topic,score,total,pct) VALUES(?,?,?,?,?,?)",
              (uid, level, topic, score, total, pct))
    c.commit(); c.close()

def get_stats(uid):
    c = _conn()
    ex = c.execute(
        "SELECT COUNT(*) total, SUM(correct) correct FROM exercise_log WHERE user_id=?", (uid,)
    ).fetchone()
    exam = c.execute(
        "SELECT COUNT(*) total, AVG(pct) avg FROM exam_log WHERE user_id=?", (uid,)
    ).fetchone()
    c.close()
    return {"ex": dict(ex), "exam": dict(exam)}

def get_leaderboard(limit=10):
    c = _conn()
    rows = c.execute(
        "SELECT first_name, xp, streak FROM users ORDER BY xp DESC LIMIT ?", (limit,)
    ).fetchall()
    c.close()
    return [dict(r) for r in rows]
