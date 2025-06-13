import os
import streamlit as st
import pandas as pd

def app():
    st.title("전기차 충전소 현황")

    st.write("현재 작업 경로:", os.getcwd())
    st.write("현재 디렉터리 파일 목록:", os.listdir())

    df = pd.read_csv("/workspaces/datascience1/charger_20230531.csv", encoding='cp949')
    st.write(df.head())
