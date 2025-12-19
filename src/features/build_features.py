def add_features(df):
    df['rolling_mean_3'] = df.groupby(['commodity','market'])['price'].transform(lambda x: x.rolling(3).mean())
    df['rolling_std_3'] = df.groupby(['commodity','market'])['price'].transform(lambda x: x.rolling(3).std())
    df['pct_change'] = df.groupby(['commodity','market'])['price'].pct_change()
    return df
