import pandas as pd

def load_hsn_data():
    return pd.read_excel("data/HSN_SAC.xlsx").rename(columns=lambda x: x.strip())
