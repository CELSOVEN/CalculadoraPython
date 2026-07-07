## Módulo para hacer operaciones

def msg_resultado(resultado, operacion):
    return(f"El resultado de la {operacion} es: {resultado}")


def calcula_con_dos_numeros(valor1, valor2, valor3):
    suma = valor1 + valor2 + valor3
    resta = valor1 - valor2 + valor3
    multiplicacion = valor1 * valor2 *  valor3
    modulo = valor1 % valor2 if valor2 != 0 else "No se puede calcular el módulo entre cero"
    potencia = valor1 ** valor2
    division = valor1 / valor2 if valor2 != 0 else "No se puede dividir entre cero"
    division_entera = valor1 // valor2  if valor2 != 0 else "No se puede dividir entre cero"
    SumaRara = valor1 + valor2 + valor3 + 10
    resultados = []
    resultados.append(msg_resultado(suma, "Suma"))
    resultados.append(msg_resultado(resta, "Resta"))
    resultados.append(msg_resultado(multiplicacion, "Multiplicación"))
    resultados.append(msg_resultado(modulo, "Módulo"))
    resultados.append(msg_resultado(potencia, "Potencia"))
    resultados.append(msg_resultado(division, "División"))
    resultados.append(msg_resultado(division_entera, "División entera"))
    resultados.append(msg_resultado(SumaRara, "Suma Rara"))
    return resultados 

def generate_html_results(resultados):
    html = "<ul>"
    for resultado in resultados:
        html += f"<li>{resultado}</li>"
    html += "</ul>"
    return html
