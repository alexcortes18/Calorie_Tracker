import mysql.connector

def get_connection(connection_location = None):
    if connection_location == None: connection_location = "NA"
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cortes1234",
        database="Calorie_Tracker"
    )
    if conn.is_connected():
        print(f"Connection Successful from {connection_location}!")
    return conn
