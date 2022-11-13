from flask import *
from models.Produto import *
from db.crud import *


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('prod_name')
    price = request.form.get('price')
    if inserir(Produto(nome=name, preco=price), engine) and name != '':
        return render_template('success.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)