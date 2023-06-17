from sqlalchemy import Column, Boolean, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///./app.db?check_same_thread=False")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    last_msg_id = Column(Integer)
    free_life = Column(Integer)
    smart_life = Column(Integer)
    simple_life = Column(Integer)
    platinum_life = Column(Integer)
    school_life = Column(Integer)
    gadjet_life = Column(Integer)
    family_life = Column(Integer)

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.free_life = 0
        self.smart_life = 0
        self.simple_life = 0
        self.platinum_life = 0
        self.school_life = 0
        self.gadjet_life = 0
        self.family_life = 0


Base.metadata.create_all(engine)
