import sqlite3

db = sqlite3.connect("cinemaInfo")
cursor = db.cursor()

cursor.execute("CREATE TABLE Movies(id INTEGER PRIMARY KEY, name TEXT, rating INTEGER)")

cursor.execute("CREATE TABLE Projections(id INTEGER PRIMARY KEY, movie_id INTEGER \
    , type TEXT, date TEXT, time TEXT, FOREIGN KEY (movie_id) REFERENCES Movies(id))")

cursor.execute("CREATE TABLE Reservations(id INTEGER PRIMARY KEY, username TEXT \
    , projection_id INTEGER, row INTEGER, col INTEGER, FOREIGN KEY (projection_id) REFERENCES Projections(id))")

name = ["Hunger Games: Catching Fire", "Wreck-it Ralph", "Her"]
rating = [7.9, 7.8, 8.3]

movie_id = [1, 1, 1, 3, 2, 2]
types = ["3D", "2D", "4DX", "2D", "3D", "2D"]
date = ["2014-04-01", "2014-04-01", "2014-04-02", "2014-04-05", "2014-04-02", "2014-04-02"]
time = ["19:10", "19:00", "21:00", "20:20", "22:00", "19:30"]

username = ["RadoRado", "RadoRado", "RadoRado", "Ivo", "Ivo", "Mysterious", "Mysterious"]
col = [1, 5, 8, 1, 2, 3, 4]
row = [2, 3, 7, 1, 1, 2, 2]
projection_id = [1, 1, 1, 3, 3, 5, 5]

for i in range(len(name)):
    cursor.execute("INSERT INTO Movies(name, rating) VALUES (?,?)", (name[i], rating[i]))

for i in range(len(movie_id)):
    cursor.execute("INSERT INTO Projections(movie_id, type, date, time) VALUES (?,?,?,?)",
        (movie_id[i], types[i], date[i], time[i]))

for i in range(len(col)):
    cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES (?,?,?,?)",
        (username[i], projection_id[i], row[i], col[i]))

db.commit()
