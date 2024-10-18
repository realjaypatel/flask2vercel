from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('index.html',title="Build Anything with Themebook", name="Jay")

@app.route("/product")
def mbsa():
    return render_template('product.html')

