import streamlit as st
import pandas as pd

df = pd.read_csv('../Dados/df_acidentes.csv')

st.title("Dataset Acidentes Trânsito")

df['ano'] = pd.to_datetime(df['data_inversa']).dt.year

sel_ano = st.selectbox("Selecione o ano:", df['ano'].unique())

df_filter = df[df['ano'] == sel_ano]

st.write(f"Ano selecionado: {sel_ano}")
st.dataframe(df_filter)