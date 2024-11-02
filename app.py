import json
from flask import Flask, render_template
app = Flask(__name__)
data = []
with open('db/product.json', 'r') as file:
    data = json.load(file)

@app.route("/")
def start():
    


    return render_template('index.html',title="Get Everything on OneLink", name="Jay",products=data['product'])

@app.route("/product")
def product():
    return render_template('product.html')

