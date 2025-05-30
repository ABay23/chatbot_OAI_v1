from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'
POSTGRES_DB_URL = 'ostgresql://testing_1/Test1234!@localhost/TodoApplicationDatabase'

# engine = create_engine(SQLALCHEMY_DATABASE_URLPO, connect_args={'check_same_thread' : False})
engine = create_engine(POSTGRES_DB_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)

Base = declarative_base()