import sqlite3

connection = sqlite3.connect("polyglot.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

result = cursor.execute("SELECT * FROM languages")

for row in result:
    print("{} - {}".format(row["id"], row["language"]))
