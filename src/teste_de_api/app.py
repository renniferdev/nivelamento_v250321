from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Carregar os dados do CSV em memória
def load_data():
    operadoras = []
    with open('operadoras.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            operadoras.append(row)
    return operadoras

operadoras_data = load_data()

@app.route('/search', methods=['GET'])
def search_operadoras():
    # Pega o parâmetro de busca da query string
    query = request.args.get('query', '').lower()
    
    # Filtra os resultados com base no parâmetro de busca
    results = [operadora for operadora in operadoras_data if query in operadora['razao_social'].lower() or query in operadora['cnpj'].lower()]
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
