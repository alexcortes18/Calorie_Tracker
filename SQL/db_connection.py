import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cortes1234",
        database="Calorie_Tracker"
    )
    if conn.is_connected():
        print("Connection Successful!")
    return conn

