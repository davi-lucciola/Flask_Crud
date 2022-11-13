import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, Float
from conf.engine import *
from sqlalchemy.orm import declarative_base

engine = create_engine()

Base = declarative_base(bind=engine)

class Produto(Base):
    __tablename__: str = 'produtos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(30), nullable=False)
    preco: float = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f'< {self.nome} - R${self.preco} >'


if engine is not None:
    if not sa.inspect(engine).has_table('produtos'): 
        Base.metadata.create_all()
    