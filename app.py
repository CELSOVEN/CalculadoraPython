
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

#Flask enviará el contenido de index.html

def inicio():
    return render_template("index.html")

app.run()


