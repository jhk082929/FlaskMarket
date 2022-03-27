from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone',      'barcode': 89321214141, 'price': 500},
        {'id': 2, 'name': 'Laptop',     'barcode': 12421251512, 'price': 900},
        {'id': 3, 'name': 'keyboard',   'barcode': 22525125121, 'price': 150}
    ]
    return render_template('market.html', items=items)