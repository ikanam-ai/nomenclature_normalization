import pandas as pd
from rapidfuzz import fuzz

df_path = 'data/new_train.csv'
df = pd.read_excel(df_path)

ksr_path = 'data/ksr_clean.csv'
ksr = pd.read_csv(ksr_path)

def similar_df(massive, seq):
    similarity = []
    for ksr_item in massive:
        similarity += [fuzz.ratio(ksr_item, seq)]
    return similarity

def similar_df_in_df(data1, seq):
    data = data1.copy()
    data['score'] = similar_df(data['record_name'], seq = seq)
    data = data.sort_values(by='score')[-3:]
    return data

def similar_df_in_ksr(data1, seq):
    data = data1.copy()
    data['score'] = similar_df(data['Наименование'], seq = seq)
    data = data.sort_values(by='score')[-3:]
    return data



