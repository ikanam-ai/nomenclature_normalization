from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_summary():
    try:
        data = request.get_json()
        predict = 'hello_timma'
        return jsonify({'predict': data})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
