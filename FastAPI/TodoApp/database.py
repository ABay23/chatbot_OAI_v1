import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'
load_dotenv()
db_url = os.getenv('POSTGRES_DB_URL')

# engine = create_engine(SQLALCHEMY_DATABASE_URLPO, connect_args={'check_same_thread' : False})
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()