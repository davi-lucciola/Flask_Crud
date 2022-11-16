from flask import *
from models.__all_models import *
from db.crud import *


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('prod_name')
    price = request.form.get('price')
    if price != '' and name != '':
        if insert(Product(product=name, price=price)):
            return render_template('success.html')
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)