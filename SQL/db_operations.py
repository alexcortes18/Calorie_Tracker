from SQL.db_connection import get_connection

def save_food_entries(entries, date):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # wipe existing rows for that date
        cur.execute("DELETE FROM food_log WHERE date=%s", (date,))
        for meal_type, food_item, calories, protein, fat, carbs in entries:
            cur.execute(
                "INSERT INTO food_log (date, meal_type, food_item, calories, protein, fat, carbs) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (date, meal_type, food_item, calories, protein, fat, carbs)
            )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def save_exercise_entries(entries, date):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM exercise_log WHERE date=%s", (date,))
        for exercise, duration, burned in entries:
            cur.execute(
                "INSERT INTO exercise_log (date, exercise, duration, calories_burned) "
                "VALUES (%s,%s,%s,%s)",
                (date, exercise, duration, burned)
            )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def save_daily_summary(date, weight, total_calories, notes):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO daily_summary (date, weight, total_calories, notes) "
            "VALUES (%s,%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE weight=%s, total_calories=%s, notes=%s",
            (date, weight, total_calories, notes, weight, total_calories, notes)
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()
