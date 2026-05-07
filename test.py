import sqlite3

DATABASE = 'fighter.db'

db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM fighter;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
db.close()