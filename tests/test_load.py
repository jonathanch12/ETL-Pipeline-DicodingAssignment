import os
import pandas as pd
from utils.load import load_to_csv

def test_load_to_csv():
    df = pd.DataFrame({
        "Title": ["Test"],
        "Price": [1600000],
        "Rating": [4.5],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Men"]
    })

    filename = "test_output.csv"
    load_to_csv(df, filename)

    assert os.path.exists(filename)

    os.remove(filename)