import sqlite3
connection = sqlite3.connect("users.db")
crsr = connection.cursor()
print("connected to database")

query="CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,username text,password text)";
query2 = """INSERT INTO user VALUES (1, "Saikat","123");"""
query3 = """INSERT INTO user VALUES (2, "Ajoy","123");"""
crsr.execute(query)
crsr.execute(query2)
crsr.execute(query3)

connection.commit()
connection.close()