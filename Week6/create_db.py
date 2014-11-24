from movie import Movie
from projection import Projection
from reservation import Reservation
from connection import Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)


def create_table_movies():
    moviecount = 3
    movies = [Movie() for i in range(moviecount)]

    name = ["Hunger Games: Catching Fire", "Wreck-it Ralph", "Her"]
    rating = [7.9, 7.8, 8.3]

    for i in range(moviecount):
        movies[i].name = name[i]
        movies[i].rating = rating[i]

    session.add_all(movies)


def create_table_projcetions():
    projectionscount = 6
    projections = [Projection() for i in range(projectionscount)]

    movie_id = [1, 1, 1, 3, 2, 2]
    types = ["3D", "2D", "4DX", "2D", "3D", "2D"]
    datetimes = [[2014, 4, 1, 19, 10], [2014, 4, 1, 19, 00], [2014, 4, 2, 21, 00],
     [2014, 4, 5, 20, 20], [2014, 4, 2, 22, 00], [2014, 4, 2, 19, 30]]

    for i in range(projectionscount):
        projections[i].movie_id = movie_id[i]
        projections[i].type = types[i]
        projections[i].datetime = datetime(*datetimes[i])

    session.add_all(projections)


def create_table_reservations():
    reservationscount = 7
    reservations = [Reservation() for i in range(reservationscount)]

    username = ["RadoRado", "RadoRado", "RadoRado", "Ivo", "Ivo", "Mysterious", "Mysterious"]
    col = [1, 5, 8, 1, 2, 3, 4]
    row = [2, 3, 7, 1, 1, 2, 2]
    projection_id = [1, 1, 1, 3, 3, 5, 5]

    for i in range(reservationscount):
        reservations[i].username = username[i]
        reservations[i].projection_id = projection_id[i]
        reservations[i].col = col[i]
        reservations[i].row = row[i]

    session.add_all(reservations)


def main():

    create_table_movies()
    create_table_projcetions()
    create_table_reservations()
    session.commit()

if __name__ == '__main__':
    main()
