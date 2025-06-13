import streamlit as st
import requests
def app():
    # 🔑 카카오 REST API 키
    KAKAO_REST_API_KEY = "69a00b850603bf7958e11ab5c9aef2ba"

    def search_places(keyword):
        url = "https://dapi.kakao.com/v2/local/search/keyword.json"
        headers = {"Authorization": f"KakaoAK {KAKAO_REST_API_KEY}"}
        params = {"query": keyword}

        res = requests.get(url, headers=headers, params=params)

        if res.status_code == 200:
            return res.json()['documents']
        else:
            st.error(f"API 오류: {res.status_code}")
            return []

    st.title("전기차 사도 되나요?")

    # 세션 상태에 입력창 개수 저장
    if "input_count" not in st.session_state:
        st.session_state.input_count = 1

    # 버튼 클릭 시 입력창 추가
    if st.button("검색창 추가하기"):
        st.session_state.input_count += 1

    results_all = []

    # 각 입력창마다 검색 처리
    for i in range(st.session_state.input_count):
        keyword = st.text_input(f"검색어 입력 {i+1}", key=f"keyword_{i}")
        results = []
        selected = None

        if keyword:
            results = search_places(keyword)
            results_all.append(results)

            if results:
                names = [f"{item['place_name']} ({item['road_address_name'] or item['address_name']})" for item in results]
                selected = st.selectbox(f"검색 결과 중 선택하세요 ({i+1})", names, key=f"select_{i}")

                if selected:
                    index = names.index(selected)
                    lat = results[index]['y']
                    lng = results[index]['x']
                    st.success(f"✅ {i+1}번 검색 결과 → 위도: {lat}, 경도: {lng}")
            else:
                st.warning(f"{i+1}번 검색 결과가 없습니다.")


