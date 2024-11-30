from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    print(f"Received data: {data}")
    # Processamento simples
    processed_data = {
        "average": (data['temperature'] + data['humidity']) / 2,
        "original": data
    }
    print(f"Processed data: {processed_data}")
    return jsonify(processed_data)

if __name__ == '__main__':
    # Escuta em todas as interfaces da rede local
    app.run(host='172.25.126.164', port=5000)