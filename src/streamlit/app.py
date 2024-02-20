import streamlit as st
import pandas as pd
st.title("""
HOLA MUNDO
hola hola hola
""")
st.header("holi")
st.markdown("*juan*")

df = pd.read_csv('train.csv')
st.dataframe(df)

for i in df.columns:
    df[i].plot(kind='hist')