from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine("sqlite:///Scores.db")


class Player(Base):

    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    place = Column(Integer)
    name = Column(String)
    score = Column(Integer)

    def __str__(self):
        return "{}: {} - {}".format(self.place, self.name, self.score)

engine = create_engine("sqlite:///Scores.db")
Base.metadata.create_all(bind=engine)
session = Session(bind=engine)


def take_highscore():
    i = 1
    for player in session.query(Player).order_by(Player.score)[0:9:-1]:
        player.place = i
        i += 1
        session.commit()
        print(player)


def save_user(name, score):
    player = Player(name=name, score=score)
    session.add(player)
    session.commit()
