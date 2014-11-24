from sqlalchemy import Column, Integer, String, Float
from connection import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)

    def __repr__(self):
        return "\n[%r] - %r : %r" % (self.id, self.name, self.rating)
