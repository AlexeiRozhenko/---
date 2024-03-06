import streamlit as st 
import pandas as pd
import plotly.express as px
import openpyxl
import os

st.set_page_config(page_title="Sales report", page_icon="📈")
st.header("Sales report")

def sales_chart(data, x_axis, y_axis, title):
  fig = px.line(data, x=x_axis, y=y_axis, title=title)
  st.plotly_chart(fig, use_container_width=True)
  
with st.sidebar:
  with open('sample_table.xlsx','rb') as file:
    st.download_button(label= 'Download Sample File',
              file_name='sample_table.xlsx',
              data=file,
              use_container_width=False)
  
  uploaded_file = st.file_uploader("Choose an XLSX file", accept_multiple_files=False)
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  with st.expander("Data preview"):
    st.dataframe(df.head())
  sales_chart(df, df["date"], df["sales"], "Sales changes")

