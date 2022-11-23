from flask import *
from models.__all_models import *
from db.crud import *


app = Flask(__name__)


# Pages Endpoints
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/cadastrar_produto', methods=['GET'])
def cadastrar_produto():
    return render_template('cadastrar_produtos.html', title='Cadastrar Produtos')

@app.route('/deletar_produto')
def deletar_produto():
    return render_template('deletar_produto.html', title='Deletar Produto')

@app.route('/atualizar_produto')
def atualizar_produto():
    return render_template('atualizar_produtos.html', title='Atualiza')

@app.route('/produtos_cadastrados', methods=['GET'])
def listar_produtos():
    return render_template(
        template_name_or_list='listar_produtos.html',
        produtos=select_all(),
        title='Produtos'
    )

# Crud Endpoints
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('prod_name')
    price = request.form.get('price')
    description = request.form.get('description')
    if price != '' and name != '':
        if insert(Product(product=name, price=price, description=description)):
            return render_template('success.html', operation='registrado'), 200
    return render_template('error.html', operation='registrar'), 404

@app.route('/update', methods=['POST'])
def update_prod():
    id = request.form.get('id')
    name = request.form.get('prod_name')
    price = request.form.get('price')
    description = request.form.get('description')
    if id != '' and name != '' and price != '':
        if update(Product(id=id, product=name, price=price, description=description)):
            return render_template('success.html', operation='atualizado')
    return render_template('error.html', operation='atualizar')

@app.route('/delete', methods=['POST'])
def delete_prod():
    id = request.form.get('id')
    if id != '':
        if delete(id):
            return render_template('success.html', operation='deletado')
    return render_template('error.html', operation='deletar')

if __name__ == '__main__':
    app.run(debug=True)