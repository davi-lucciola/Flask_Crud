from sqlalchemy import Column, String, Integer, DECIMAL
from models.model_base import Base
from typing import Optional


class Product(Base):
    '''
    atributes:
        id: int
        product: str
        price: float
        description: Opitional[str]
    '''
    __tablename__ = 'products'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    product: str = Column(String(30), nullable=False)
    price: float = Column(DECIMAL(6, 2), nullable=False)
    description: Optional[str] = Column(String(60))

    def __repr__(self) -> str:
        return f'<{self.product} - R${self.price}>'