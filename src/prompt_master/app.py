from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from fuzzywuzzy import fuzz
import requests
import Levenshtein
import pandas as pd
from flask import Flask, request, jsonify
from similar import similar_df_in_df


class PromptMaster:
    def __init__(self, api_url="http://83.143.66.61:27368/generate"):
        self.api_url = api_url
        with open("prompt_list.txt", "r", encoding="utf-8") as file:
            self.prompt = file.read()

    def get_request(self, text_list):
        prompt = self.prompt.format(*text_list)
        payload = {"prompt": prompt}
        response = requests.post(self.api_url, json=payload)
        generated_text = response.text
        return generated_text

app = Flask(__name__)
PM = PromptMaster()

@app.route('/generate', methods=['POST'])
def generate_summary():
    try:
        data = request.get_json()
        text_to_gen = data['text_list']
        predict = PM.get_request(text_to_gen)
        return jsonify({'predict': predict})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='83.143.66.61', port=27370)
