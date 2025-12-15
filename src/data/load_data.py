import pandas as pd

def load_raw_data(path = "../data/raw/wfp_food_prices.csv"):
    """Load raw food prices data from CSV file."""
    df = pd.read_csv(path)
    return df
