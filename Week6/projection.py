from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import Base


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    datetime = Column(DateTime)

    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="projections")

    def __repr__(self):
        return "\n[%r] - %r  %r  %r" % (self.id, self.movie_id, self.type,
            str(self.datetime))
