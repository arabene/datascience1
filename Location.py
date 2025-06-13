import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import os

def app():
    st.title("전기차 충전소 현황")

    # 현재 작업 디렉토리와 파일 목록 출력(디버깅용)
    st.write("현재 작업 경로:", os.getcwd())
    st.write("현재 디렉토리 파일 목록:", os.listdir())

    # CSV 읽기
    df = pd.read_csv("charger_20230531.csv", encoding='euc-kr')

    st.write(df.head())
