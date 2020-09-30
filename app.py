from flask import Flask
from src.products import Products

app = Flask(__name__)

@app.route('/')
def start():
    return 'Estamos on compare, ahora si!!!'

app.run(host='127.0.0.1', port=4000, debug=True)