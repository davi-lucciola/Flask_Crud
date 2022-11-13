import sqlalchemy as sa
from sqlalchemy.future import Engine
from sqlalchemy.orm import sessionmaker
from typing import Optional


CONX_STR = 'sqlite:///./db/loja.db'

def create_engine():
    global CONX_STR

    # Creating Engine
    __engine = sa.create_engine(CONX_STR)
    return __engine

def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    return session