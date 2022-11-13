from conf.engine import *
from models.Produto import Produto


def inserir(produto: Produto, engine: Engine):
    with create_session(engine) as session:
        try:
            session.add(produto)
        except Exception as err:
            session.rollback()
            return False
        else:
            session.commit()
            return True

def select_all(engine: Engine):
    with create_session(engine) as session:
        try:
            query_all: list[Produto] = session.query(Produto)
        except Exception as err:
            raise err('Não foi possivel Selecionar Tudo')
        else:
            return query_all