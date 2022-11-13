from models.Produto import *
from db.crud import *

produtos: list[Produto] = list(select_all(engine))

print('-='*14)
print('ID  |  PRODUTO  | PREÇO')
print('-='*14)
for produto in produtos:
    print(f'{produto.id:<4}|{produto.nome:^11}| R${produto.preco:<4}')