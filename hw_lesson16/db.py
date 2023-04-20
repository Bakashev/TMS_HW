from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  MetaData

database = "postgresql://postgres:123456@localhost:5432/lesson_test"
engine = None
Session = sessionmaker(autoflush=False, bind=engine)

def configurate_engine():
    global engine
    if engine is None:
        engine = create_engine(database)
        Session.configure()

