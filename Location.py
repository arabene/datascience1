import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd

def app():
    st.title("전기차 충전소 현황")

    df = pd.read_csv("/workspaces/datascience1/charger_20230531.csv", encoding='euc-kr')


# '위도경도' 열을 쉼표(,) 기준으로 분리하여 '위도', '경도' 두 개의 새로운 열 만들기
    df[['위도', '경도']] = df['위도경도'].str.split(',', expand=True)

    # 문자열 상태일 수 있으니 실수(float)로 변환
    df['위도'] = df['위도'].astype(float)
    df['경도'] = df['경도'].astype(float)

    # 필요하면 원본 '위도경도' 열은 삭제 가능
    # df = df.drop(columns=['위도경도'])

    print(df.head())