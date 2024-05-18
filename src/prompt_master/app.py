from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from fuzzywuzzy import fuzz
import requests
import Levenshtein
import pandas as pd
from flask import Flask, request, jsonify


class PromptMaster:
    def __init__(self, api_url="http://83.143.66.61:27369/generate"):
        self.api_url = api_url
        with open("prompt_master/prompt_list.txt", "r", encoding="utf-8") as file:
            self.prompt = file.read()

    def get_request(self, text_list):
        prompt = self.prompt.format(*text_list)
        payload = {"prompt": prompt}
        response = requests.post(self.api_url, json=payload)
        generated_text = response.text
        return generated_text

