from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('index.html',title="Get Everything on Onelink", name="Jay")

@app.route("/product")
def product():
    return render_template('product.html')

