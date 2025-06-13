import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import os

def app():
    st.title("전기차 충전소 현황")

    # CSV 읽기
    df = pd.read_csv("charger_20230531.csv", encoding='utf-8')

    st.write(df.head())
