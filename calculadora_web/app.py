from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = ""
    if request.method == "POST":
        expressao = request.form["expressao"]
        try:
            resultado = eval(expressao)
        except:
            resultado = "Erro"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
