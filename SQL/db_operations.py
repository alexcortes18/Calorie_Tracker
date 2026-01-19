from SQL.db_connection import get_connection
from PyQt6.QtWidgets import (QMessageBox)

def save_food_entries(entries, date):
    conn = get_connection("saving food!")
    cur = conn.cursor()
    try:
        for meal_type, food_item, calories, protein, fat, carbs in entries:
            cur.execute(
                "UPDATE food_log "
                "SET calories=%s, protein=%s, fat=%s, carbs=%s "
                "WHERE date=%s AND meal_type=%s AND food_item=%s",
                (calories, protein, fat, carbs, date, meal_type, food_item)
            )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def save_exercise_entries(entries, date):
    conn = get_connection("saving exercises!")
    cur = conn.cursor()
    try:
        for exercise, duration, burned in entries:
            cur.execute(
                "UPDATE exercise_log "
                "SET duration=%s, calories_burned=%s "
                "WHERE date=%s AND exercise=%s",
                (duration, burned, date, exercise)
            )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def save_daily_summary(date, weight, total_calories, notes):
    conn = get_connection("saving daily summary")
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

def get_food_entries(selected_date=None):
    conn = None
    cursor = None
    try:
        conn = get_connection("Food Log")
        cursor = conn.cursor()

        if selected_date:
            cursor.execute(
                "SELECT meal_type, food_item, calories, protein, fat, carbs "
                "FROM food_log WHERE date = %s",
                (selected_date,)
                )
        return cursor.fetchall()
    except Exception as e:
        QMessageBox.critical(None, "Database Error", str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()   
        
def get_exercises_entries(selected_date=None):
    conn = None
    cursor = None
    try:
        conn = get_connection("Load Exercises")
        cursor = conn.cursor()

        if selected_date:
            cursor.execute(
                "SELECT exercise, duration, calories_burned "
                "FROM exercise_log WHERE date = %s",
                (selected_date,)
            )

        return cursor.fetchall()
    except Exception as e:
        QMessageBox.critical(None, "Database Error", str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_weight_entry(selected_date=None):
    conn = None
    cursor = None
    
    try:
        conn = get_connection("Load Weights")
        cursor = conn.cursor()
        
        if selected_date:
            cursor.execute(
                "SELECT weight FROM daily_summary "
                "WHERE date = %s",
                (selected_date,)
            )
        return cursor.fetchone() # 1 row expected
    except Exception as e:
        QMessageBox.critical(None, "Database Error", str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_summary_entries(selected_date=None):
    conn = None
    cursor = None
    try:
        conn = get_connection("Load Summary")
        cursor = conn.cursor()

        # totals from food_log
        food_totals = (0, 0, 0, 0)  # calories, protein, fat, carbs
        if selected_date:
            cursor.execute(
                "SELECT COALESCE(SUM(calories),0), COALESCE(SUM(protein),0), "
                "COALESCE(SUM(fat),0), COALESCE(SUM(carbs),0) "
                "FROM food_log WHERE date=%s",
                (selected_date,)
            )
            food_totals = cursor.fetchone()

        # totals from exercise_log
        exercise_total = 0
        if selected_date:
            cursor.execute(
                "SELECT COALESCE(SUM(calories_burned),0) "
                "FROM exercise_log WHERE date=%s",
                (selected_date,)
            )
            exercise_total = cursor.fetchone()[0]

        # net calories = food calories - exercise calories
        net_calories = food_totals[0] - exercise_total
        
        return {
            "calories": food_totals[0],
            "protein": food_totals[1],
            "fat": food_totals[2],
            "carbs": food_totals[3],
            "exercise": exercise_total,
            "net": net_calories
        }

    except Exception as e:
        QMessageBox.critical(None, "Database Error", str(e))
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_notes(selected_date=None):
    conn = None
    cursor = None
    try:
        conn = get_connection("Load Summary")
        cursor = conn.cursor()
        
        # Notes from that day if any
        note = ""
        if selected_date:
            cursor.execute(
                "SELECT notes "
                "FROM daily_summary WHERE date=%s",
                (selected_date,)
            )
            note = cursor.fetchone()[0]
        return note
    
    except Exception as e:
        QMessageBox.critical(None, "Database Error", str(e))
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    