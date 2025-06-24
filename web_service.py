from flask import Flask

app = Flask(__name__)

# This is the root route
@app.route("/")
def root():
    return "<p>Please press <a href=poks>here</a>."

@app.route("/poks")
def poks():
    return "<h1>Poks</h1><p>This is the content of the address /poks.</p>"

