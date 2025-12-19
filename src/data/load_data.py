import pandas as pd
from pathlib import Path

def load_raw_data():
    """Load raw food prices data from CSV file."""
    data_path = r"C:\Users\siddi\projects\food-price-anomaly-detector\dataset\raw\wfp_food_prices_ind.csv"

    df = pd.read_csv(data_path)
    
    # drop the first row
    df = df.iloc[1:].reset_index(drop=True)


    # convert other columns to their respective data types
    df = df.astype(
        {
            'admin1': 'string',
            'admin2': 'string',
            'market': 'string',
            'category': 'string',
            'commodity': 'string',
            'unit': 'string',
            'priceflag': 'string',
            'pricetype': 'string',
            'currency': 'string',
            'market_id': 'int',
            'commodity_id': 'int',
            'latitude': 'float',
            'longitude': 'float',
            'price': 'float',
            'usdprice': 'float'
        }
    )

    #convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    return df


