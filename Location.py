import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

def app():
    st.title("전기차 충전소 현황")

    # 1. 데이터 로드
    df = pd.read_csv("charger_20230531.csv", encoding='cp949')

    # 2. 위도경도 분리 (문자열 분리 → 공백 제거 → 실수형 변환)
    df[['위도', '경도']] = df['위도경도'].str.split(',', expand=True)
    df['위도'] = pd.to_numeric(df['위도'].str.strip(), errors='coerce')
    df['경도'] = pd.to_numeric(df['경도'].str.strip(), errors='coerce')

    # 3. NaN 제거 (중요!)
    df1 = df[['충전소명', '주소', '위도', '경도']].dropna(subset=['위도', '경도'])

    # 4. 지도 생성
    map = folium.Map(location=[df1['위도'].mean(), df1['경도'].mean()], zoom_start=11)
    marker_cluster = MarkerCluster().add_to(map)

    # 5. 마커 추가
    for idx, row in df1.iterrows():
        try:
            folium.Marker(
                location=[row['위도'], row['경도']],
                popup=row['충전소명']
            ).add_to(marker_cluster)
        except ValueError:
            st.warning(f"위치 값 오류 (index={idx}): 위도={row['위도']}, 경도={row['경도']}")

    folium_static(map)
