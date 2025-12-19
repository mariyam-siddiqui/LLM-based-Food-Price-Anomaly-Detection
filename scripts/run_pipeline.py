from src.data.load_data import load_raw_data
from src.data.preprocess import clean_data
from src.features.build_features import add_features
from src.models.anomaly_detector import detect_anomalies

df = load_raw_data()
df = clean_data(df)
df = add_features(df)
df = detect_anomalies(df)

df.to_csv("output/anomalies/output.csv", index=False)
print("Pipeline ran successfully!")
