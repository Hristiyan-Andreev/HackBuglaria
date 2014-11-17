import sqlite3


def show_movies(db):
    cursor = db.cursor
    result = cursor.execute("SELECT id, name, rating FROM Movies ORDER BY rating")
    print("\nCurrent movies: ")
    for row in result:
        print("{} - {} ({})".format(row["id"], row["name"], row["rating"]))


def show_movie_projections(db, movie_id):
    cursor = db.cursor
    result = cursor.execute("SELECT id, date, time, type FROM Projections \
    WHERE id = ? ORDER BY date", movie_id)
    print("\nProjections for your movie:\n")
    for row in result:
        print("{} - {} {} ({})".format(row["id"], row["date"], row["time"], row["type"]))


def make_a_reservation(db):
    print("\nStep1 (Identity): ")
    user = input("Choose a name user!: ")
    print("\nStep1 (Identity): ")
    tickets = input("Choose number of tickets!: ")

    show_movies(db)
    print("\nStep2 (Movie): ")
    movie_id = input("Choose a movie: ")

    show_movie_projections(db, movie_id)
    projection = input("Step2 (Projection): Choose a projection:")


def main():
    db = sqlite3.connect("cinemaInfo")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    seats = {}
    matrix = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

    result = cursor.execute("SELECT id FROM Projections")
    for row in result:
        seats[row["id"]] = matrix

if __name__ == '__main__':
    main()
