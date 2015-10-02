from flask import Flask, session, g, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"