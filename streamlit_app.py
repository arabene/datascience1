import streamlit as st

st.set_page_config(
    page_title="내 스트림릿 앱",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"  # << 이 줄이 중요!
)

from Home import app as home_app
#from Location import app as location_app

PAGES = {
    "메인": home_app,
   # "충전소 위치": location_app,
}

st.sidebar.title("데싸 기말")
selection = st.sidebar.radio("페이지 선택", list(PAGES.keys()))

page = PAGES[selection]
page()

