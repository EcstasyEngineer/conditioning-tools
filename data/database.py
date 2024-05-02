# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

Base = declarative_base()

def get_engine():
    engine = create_engine(settings['storage']['url'])
    Base.metadata.create_all(engine)  # Create tables if they don't exist
    return engine

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
