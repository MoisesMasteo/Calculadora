from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    try:
        if request.method == 'POST':
                peso = float(request.form['peso'])
                altura = float(request.form['altura'])/100
                imc = round(peso / (altura * altura), 2)
                tipo = ""
                if imc < 18.5:
                    tipo = "Delgado"
                elif imc > 18.5 and imc < 25:
                    tipo = "Normal"
                elif imc > 25 and imc < 30:
                    tipo = "Con sobrepeso"
                else:
                    tipo = "Obeso"
                return render_template('resultado.html', imc=imc, tipo=tipo)
        return render_template('index.html')
    except ValueError:
         return render_template('index.html', texto="No puedes escribir algo que no sea numeros.")
if __name__ == '__main__':
    app.run(debug=True)