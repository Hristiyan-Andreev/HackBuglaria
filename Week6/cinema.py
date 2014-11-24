from connection import Base
from movie import Movie
from projection import Projection
from reservation import Reservation
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


class Cinema:

    def __init__(self, session):
        self.session = session

    def show_movies(self):
        movies = self.session.query(Movie).order_by(Movie.rating).all()
        print("\nOur movies are:")
        return movies

    def show_projections(self, id):
        projections = self.session.query(Projection).filter(Projection.movie_id == id).all()
        moviename = self.session.query(Movie).filter(Movie.id == id).first()
        print("\nOur projections for {} are:".format(moviename.name))
        return projections

    def make_reservation(self):
        print("\nStep1 (Identity): ")
        user = input("Choose a name user!: ")
        print("\nStep1 (Identity): ")
        tickets = input("Choose number of tickets!: ")

        self.show_movies()
        print("\nStep2 (Movie): ")
        movie_id = input("Choose a movie: ")

        projection_id = input("Step2 (Projection): Choose a projection:")
        self.show_projections(projection_id)




def main():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    cinema1 = Cinema(session)

    print(cinema1.show_movies())
    print(cinema1.show_projections(2))

if __name__ == '__main__':
    main()
