from models.__all_models import *
from db.crud import *

produtos: list[Product] = list(select_all())

print('-='*14)
print('ID  |  PRODUTO  | PREÇO')
print('-='*14)
for produto in produtos:
    print(f'{produto.id:<4}|{produto.product:^11}| R${produto.price:<4}')