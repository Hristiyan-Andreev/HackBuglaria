

class Player(Base):

    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    place = Column(Integer)
    name = Column(String)
    score = Column(Integer)

    def __repr__(self):
        return "{}: {} - {}".format(self.place, self.name, self.score)
