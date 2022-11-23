from db.session_db import create_session
from models.__all_models import *


def insert(prod: Product) -> bool:
    '''
    Insert a Product in a DB with SQL Alchemy
    '''
    with create_session() as session:
        try:
            session.add(prod)
            session.commit()
        except Exception as err:
            print(err)
            session.rollback()
            return False
        else:
            return True

def delete(id: int) -> bool:
    '''
    Delete a Product in a DB with SQL Alchemy
    '''
    with create_session() as session:
        try:
            prod_to_del = session.query(Product).filter_by(id=id).first()
            session.delete(prod_to_del)
            session.commit()
        except Exception as err:
            print(err)
            session.rollback()
            return False
        else:
            return True

def update(prod_updated: Product) -> bool:
    with create_session() as session:
        try:
            prod_to_update: Product = session.query(Product).get(prod_updated.id)
            prod_to_update.product = prod_updated.product
            prod_to_update.price = prod_updated.price
            prod_to_update.description = prod_to_update.description
            session.commit()
        except Exception as err:
            print(err)
            session.rollback()
            return False
        else:
            return True

def select_all() -> list[Product]:
    '''
    Equivalent -> "SELECT * FROM products;"
    '''
    with create_session() as session:
        try:
            query_all: list[Product] = session.query(Product).all()
        except Exception as err:
            raise err('Não foi possivel Selecionar Tudo')
        else:
            return query_all