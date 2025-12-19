def clean_data(df):
    '''Preprocess the food prices dataframe.'''

    # drop rows with missing values
    df = df.dropna()

    # turn date to day, month and year columns
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    # Rename columns
    df.rename(columns= {
        'admin1' : 'state',
        'admin2' : 'city'
    }, inplace=True)

    # Standardize units
    df.loc[df['unit'] == '100 KG', 'price'] = df.loc[df['unit'] == '100 KG', 'price'] / 100
    df.loc[df['unit'] == '100 KG', 'usdprice'] = df.loc[df['unit'] == '100 KG', 'usdprice'] / 100
    df.loc[df['unit'] == '100 KG', 'unit'] = 'KG'

    # Create a new column called sub_category by removing brackets from commodity
    df['sub_category'] = df['commodity'].str.replace(r"\s*\(.*\)","", regex=True)

    # remove any duplicate rows
    df.drop_duplicates(inplace=True)

    return df