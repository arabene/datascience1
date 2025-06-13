import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd

def app():
    st.title("전기차 충전소 현황")

    df = pd.read_csv("/mount/src/datascience1/charger_20230531.csv", encoding='cp949')

    st.dataframe(df, height=200)

    df[["lat","lon"]] = df[["위도","경도"]]

    m = folium.Map(location=[35.1799817, 128.1076213], zoom_start=13)

    marker_cluster = MarkerCluster().add_to(m)

    for idx, row in df.iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=row["설치장소"],
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(marker_cluster)

    folium_static(m)
