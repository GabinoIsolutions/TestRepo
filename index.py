from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/lorem")
def lorem():
    return render_template('lorem.html')

@app.route("/ipsum")
def ipsum():
    return render_template('ipsum.html')

@app.route("/dolor")
def dolor():
    return render_template('dolor.html')

@app.route("/amet")
def amet():
    return render_template('amet.html')

