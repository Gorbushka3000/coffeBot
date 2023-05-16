from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_NAME = "vsegdaCoffe.sqlite"

engine = create_engine(f'sqlite:///D:/Programming/Python/MyProject/vsegdaCoffe.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)