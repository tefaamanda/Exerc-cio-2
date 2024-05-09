from flask import Flask, render_template, request # Declara as variáveis.

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html', maior='', menor='', media='') # Conecta o html ao python.

@app.route('/resultado', methods=['POST']) # Define método 'post' e resultado.
def resultado():
    maior = 0  # Define valor do maior (equivalente a 0).
    menor = 999  # Define valor do menor (equivalente a 999).
    soma = 0  # Define valor da soma (equivalente a 0).
    qtd = 0  # Define valor da quantidade (equivalente a 0).

    for qtd in range(10): # Enquanto a quantidade for 10.
        numero = int(request.form['numero' + str(qtd)]) # Insere o dígito.
        if numero > maior:  # Se o maior número for identificado.
            maior = numero  # Declara o maior número.
        if numero < menor:  # Se o menor número for identificado.
            menor = numero  # Declara o menor número.
        soma += numero  # Calcula a soma dos número.
        qtd += 1  # Adiciona à quantidade de número no loop (até 10).

    media = soma / qtd  # Calcula a média dos valores.
    return render_template('index.html', maior=maior, menor=menor, media=media) # Imprime o resultado.

if __name__ == '__main__':
    app.run(debug=True)