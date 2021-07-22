import sqlite3

def create_table():
    conn = sqlite3.connect("file.db")#connecting to the database file/ creating a database file if needed
    cur = conn.cursor()#creating a cursor object
    cur.execute(" CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_table(item, quantity, price):
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()
    conn.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()

#insert_table("Water Glass", 8, 5)

update(15, 8.5, "Beer Mug")
print(view())
