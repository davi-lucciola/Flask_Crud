from flask import *
from models.__all_models import *
from db.crud import *


app = Flask(__name__)


# Pages Endpoints
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/cadastrar_produto', methods=['GET'])
def cadastrar_produto():
    return render_template('cadastrar_produtos.html')

@app.route('/produtos_cadastrados', methods=['GET'])
def listar_produtos():
    pass

@app.route('/atualizar produto:')

# Apis Endpoints
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('prod_name')
    price = request.form.get('price')
    if price != '' and name != '':
        if insert(Product(product=name, price=price)):
            return render_template('success.html')
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)