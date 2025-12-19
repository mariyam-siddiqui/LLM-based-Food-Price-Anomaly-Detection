from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05, random_state=42)

    features = df[['rolling_mean_3', 'rolling_std_3', 'pct_change']].fillna(0)
    df['anomaly_score'] = model.fit_predict(features)
    
    df['is_anomaly'] = df['anomaly_score'].apply(lambda x: 1 if x == -1 else 0)
    return df

