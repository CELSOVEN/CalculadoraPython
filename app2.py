from flask import Flask, request
from flask import Flask, render_template
from os import system

system("cls")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def inicio():
    if request.method == "POST":
        valor1 = request.form["valor1"]
        valor2 = request.form["valor2"]
        resultado = float(valor1) + float(valor2) 
                       # Process the submitted values
        return f"Values submitted: {valor1}, {valor2}. \
        <br> <br> Sum Result: {resultado}"
    return render_template("index2.html")

if __name__ == "__main__":
        app.run()

