import sqlite3

conn = sqlite3.connect('nova.db')


def customer_control():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()
    if rows:
        cursor.execute("SELECT name FROM customer WHERE deger = 1")
        rows = cursor.fetchall()
        if rows:
            names = [row[0] for row in rows]
            return names
        else:
            return "not 1"
    else:
        return "not data"
