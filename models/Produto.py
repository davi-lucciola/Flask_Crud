from sqlalchemy import Column, String, Integer, Float
from models.model_base import *


class Produto(Base):
    __tablename__: str = 'produtos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(30), nullable=False)
    preco: float = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f'< {self.nome} - R${self.preco} >'

    