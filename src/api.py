from flask import Flask, request, jsonify
from prompt_master.app import PromptMaster
from prompt_master.similar import similar_df_in_df, similar_df_in_ksr
import pandas as pd

app = Flask(__name__)
PM = PromptMaster()

df_path = 'data/new_train.csv'
df = pd.read_csv(df_path).reset_index(drop=True)

ksr_path = 'data/ksr_clean.csv'
ksr = pd.read_csv(ksr_path).reset_index(drop=True)

@app.route('/generate', methods=['POST'])
def generate_summary():
    try:
        data = request.get_json()
        req = data['req']
        res = similar_df_in_df(df, req)[['record_name', 'ref_name']]
        record_names = res['record_name'].tolist()
        ref_names = res['ref_name'].tolist()
        result_array = list(sum(zip(record_names, ref_names), ()))
        data = PM.get_request(result_array + [req])
        result = similar_df_in_ksr(ksr, data).tolist()
        return jsonify({'predict': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27370)