from conf.config_engine import create_session, __engine
from models.Produto import Produto


def insert(produto: Produto):
    global __engine
    with create_session(__engine) as session:
        try:
            session.add(produto)
        except Exception as err:
            session.rollback()
            return False
        else:
            session.commit()
            return True

def select_all():
    global __engine
    with create_session(__engine) as session:
        try:
            query_all: list[Produto] = session.query(Produto)
        except Exception as err:
            raise err('Não foi possivel Selecionar Tudo')
        else:
            return query_all