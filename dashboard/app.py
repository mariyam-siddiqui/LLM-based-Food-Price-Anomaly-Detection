import streamlit as st
import pandas as pd
import os


df = pd.read_csv(r"C:\Users\siddi\projects\food-price-anomaly-detector\output\anomalies\output.csv")
# df.head()

st.title("📈 Food Price Anomaly Detector")
commodity = st.selectbox("Select commodity", df['commodity'].unique())

filtered = df[df['commodity'] == commodity]
st.line_chart(filtered[['date','price']].set_index('date'))
st.dataframe(filtered[filtered['is_anomaly']==1])
