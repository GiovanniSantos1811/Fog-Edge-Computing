from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json # Extrai o formato da requisicao HTTP
    print(f"Received data: {data}")
    
    # Processamento de dados simples 
    classificacao = 'nao classificado'

    if data['sensor_data'] > 70 and data['sensor_data'] < 80:
        classificacao = 'baixo risco'
    if data['sensor_data'] > 80 and data['sensor_data'] < 90:
        classificacao = 'medio risco'
    if data['sensor_data'] > 90:
        classificacao = 'alto risco'

    processed_data = {
        "classificacao": classificacao,
    }
    
    print(f"Processed data: {processed_data}")
    return jsonify(processed_data)

if __name__ == '__main__':
    # Escuta em todas as interfaces da rede local
    app.run(host='0.0.0.0', port=5000)
