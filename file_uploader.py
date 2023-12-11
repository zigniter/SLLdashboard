import streamlit as st
import pandas as pd


def fileUploader():

    uploaded_file = st.file_uploader("Upload your file here...", type=['csv'])

    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
