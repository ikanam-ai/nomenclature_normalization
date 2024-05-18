from flask import Flask, request, jsonify
from model import Model

app = Flask(__name__)

model_gpt = Model()

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        print(prompt)

        generated_text = model_gpt.interact(prompt)
        print(generated_text)

        return generated_text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27368)