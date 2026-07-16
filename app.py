import os
import calculadora_service as md

from flask import Flask, request
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def inicio():
    if request.method == "POST":
        valor1 = request.form["valor1"]
        valor2 = request.form["valor2"]
        valor3 = request.form["valor3"]
        resultados = md.calcula_con_dos_numeros(float(valor1), float(valor2), float(valor3))
        html_results = md.generate_html_results(resultados)
        return html_results
    return render_template("index.html")


#Cuando se trabaja en la nube se utilizan estas líneas de código
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
