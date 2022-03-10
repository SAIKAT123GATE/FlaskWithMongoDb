import sqlite3
connection=sqlite3.connect("users.db")
cursor=connection.cursor();
query2 = """INSERT INTO items VALUES (2, "Guitar",11);"""
# create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text, price real)"
cursor.execute(query2)
connection.commit()
connection.close()