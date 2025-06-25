import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="감정 기반 플레이리스트 생성기", page_icon="🎧", layout="centered")

# 기분별 플레이리스트 이름 + Spotify 링크 매핑
mood_data = {
    "행복 😊": {
        "names": [
            "햇살 속 산책", "레몬소다 댄스", "구름 위 발걸음", "행복 바이브 믹스", "미소를 부르는 멜로디"
        ],
        "color": "#FFF8DC",  # Light yellow
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"
    },
    "슬픔 😢": {
        "names": [
            "비 오는 날의 감성", "텅 빈 방과 음악", "조용한 눈물", "회색빛 멜로디", "어느 날의 이별"
        ],
        "color": "#E0E0E0",  # Gray
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR"
    },
    "화남 😤": {
        "names": [
            "폭발하는 베이스", "분노 해소용 트랙", "불꽃 질주 사운드", "드럼 앤 분노", "사운드 펀치"
        ],
        "color": "#FFCCCC",  # Light red
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP"
    },
    "집중 🧠": {
        "names": [
            "Deep Focus Zone", "몰입의 미학", "코딩 전용 BGM", "잡생각 차단 모드", "한 줄 한 줄 집중"
        ],
        "color": "#D0E8F2",  # Light blue
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY"
    },
    "설렘 💖": {
        "names": [
            "심장 두근두근", "첫눈과 너", "고백 전야", "설레는 버스 창가", "커피향 감성 트랙"
        ],
        "color": "#FFE0F0",  # Pink
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX6Fpu5zxHZPH"
    },
    "피곤 😴": {
        "names": [
            "잠들기 5분 전", "하품 유발 BGM", "눈 감으면 재생되는 음악", "조용한 밤", "수면 유도 플레이리스트"
        ],
        "color": "#F0F8FF",  # Light lavender
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWZd79rJ6a7lp"
    },
    "외로움 🌙": {
        "names": [
            "혼자 걷는 밤길", "달빛 아래 나", "조용한 새벽 감성", "누군가 그리운 밤", "고요 속 나 혼자"
        ],
        "color": "#F5F5F5",  # Soft gray
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX1htCFhfVtyK"
    },
    "기대감 ✨": {
        "names": [
            "새로운 시작", "내일이 기대되는 음악", "두근두근 프로젝트", "첫 출근 BGM", "도전의 서막"
        ],
        "color": "#E6FFE6",  # Light green
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX4fpCWaHOned"
    },
}

# CSS 스타일 동적 적용
def apply_background(color_hex):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color_hex};
        }}
        .playlist-card {{
            background-color: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            text-align: center;
            font-size: 1.4rem;
        }}
        .spotify-btn {{
            text-align: center;
            margin-top: 1rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 헤더
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🎧 기분별 플레이리스트 생성기</h1>", unsafe_allow_html=True)
st.markdown("지금의 감정에 어울리는 감성적인 플레이리스트 이름과 음악을 추천해드릴게요 ✨")

# 기분 선택
mood_choice = st.selectbox("👉 현재 기분을 선택하세요:", list(mood_data.keys()))

# 버튼 클릭 시 처리
if st.button("🎲 이름 생성하기"):
    mood = mood_data[mood_choice]
    apply_background(mood["color"])
    playlist_name = random.choice(mood["names"])
    
    st.markdown(f"""
        <div class="playlist-card">
            🎵 <strong>{playlist_name}</strong>
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown(
            f"""
            <div class="spotify-btn">
                👉 <a href="{mood['spotify']}" target="_blank">
                <button style="background-color:#1DB954; color:white; border:none; padding:10px 20px; border-radius:10px; cursor:pointer;">
                    🎶 이 기분에 어울리는 Spotify 트랙 듣기
                </button></a>
            </div>
            """,
            unsafe_allow_html=True
        )




if st.button("이름 생성하기"):
    playlist_name = random.choice(mood_playlists[mood])
    st.success(f"✨ 추천 플레이리스트 이름: **{playlist_name}**")

