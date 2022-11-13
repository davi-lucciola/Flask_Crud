from models.Produto import *
from db.crud import *


while True:
    resp = input('Deseja Adicionar Produtos? [S/N] -> ').lower()[0]
    if resp == 'n':
        break
    name = input('Digite o nome do produto: ')
    price = input('Digite o preco do produto: ')


    if inserir(Produto(nome=name, preco=price), engine):
        print('Produto adicionado com sucesso!')
    else:
        print('Não foi possivel adicionar o produto!')


print(list(select_all(engine)))