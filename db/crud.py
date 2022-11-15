from db.session_db import create_session
from models.__all_models import *


def insert(produto: Product):
    with create_session() as session:
        try:
            session.add(produto)
        except Exception as err:
            session.rollback()
            return False
        else:
            session.commit()
            return True

def select_all():
    with create_session() as session:
        try:
            query_all: list[Product] = session.query(Product)
        except Exception as err:
            raise err('Não foi possivel Selecionar Tudo')
        else:
            return query_all