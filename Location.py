import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

def app():
    st.title("전기차 충전소 현황")

    df = pd.read_csv("charger_20230531.csv", encoding='cp949')

    # 위도경도 분리: 문자열로부터 분리
    df[['위도', '경도']] = df['위도경도'].str.split(',', expand=True)

    # 공백 제거 및 float 변환 (에러 방지용)
    df['위도'] = pd.to_numeric(df['위도'].str.strip(), errors='coerce')
    df['경도'] = pd.to_numeric(df['경도'].str.strip(), errors='coerce')

    # NaN 제거
    df1 = df[['충전소명', '주소', '위도', '경도']].dropna(subset=['위도', '경도'])

    # 지도 생성
    map = folium.Map(location=[df1['위도'].mean(), df1['경도'].mean()], zoom_start=11)
    marker_cluster = MarkerCluster().add_to(map)

    for idx, row in df1.iterrows():
        folium.Marker(
            location=[row['위도'], row['경도']],
            popup=row['충전소명']
        ).add_to(marker_cluster)

    folium_static(map)
