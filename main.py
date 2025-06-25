import streamlit as st
import random

# 앱 설정
st.set_page_config(page_title="기분별 플레이리스트 생성기", page_icon="🎧", layout="centered")

# 기분별 플레이리스트 이름 모음
mood_playlists = {
    "행복 😊": [
        "햇살 속 산책", "레몬소다 댄스", "구름 위 발걸음", "행복 바이브 믹스", "미소를 부르는 멜로디"
    ],
    "슬픔 😢": [
        "비 오는 날의 감성", "텅 빈 방과 음악", "조용한 눈물", "회색빛 멜로디", "어느 날의 이별"
    ],
    "화남 😤": [
        "폭발하는 베이스", "분노 해소용 트랙", "불꽃 질주 사운드", "드럼 앤 분노", "사운드 펀치"
    ],
    "집중 🧠": [
        "Deep Focus Zone", "몰입의 미학", "코딩 전용 BGM", "잡생각 차단 모드", "한 줄 한 줄 집중"
    ],
    "설렘 💖": [
        "심장 두근두근", "첫눈과 너", "고백 전야", "설레는 버스 창가", "커피향 감성 트랙"
    ],
    "피곤 😴": [
        "잠들기 5분 전", "하품 유발 BGM", "눈 감으면 재생되는 음악", "조용한 밤", "수면 유도 플레이리스트"
    ],
    "외로움 🌙": [
        "혼자 걷는 밤길", "달빛 아래 나", "조용한 새벽 감성", "누군가 그리운 밤", "고요 속 나 혼자"
    ],
    "기대감 ✨": [
        "새로운 시작", "내일이 기대되는 음악", "두근두근 프로젝트", "첫 출근 BGM", "도전의 서막"
    ]
}

# 스타일 꾸미기
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #6C63FF;
        margin-bottom: 20px;
    }
    .playlist {
        background-color: #F4F4F8;
        padding: 1.5rem;
        border-radius: 20px;
        font-size: 24px;
        text-align: center;
        color: #333;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🎧 기분별 플레이리스트 생성기</div>', unsafe_allow_html=True)

st.markdown("지금 당신의 기분에 어울리는 플레이리스트 이름을 추천해드릴게요 💡")

# 기분 선택
mood = st.selectbox("👇 현재 기분을 선택하세요", list(mood_playlists.keys()))

# 결과 출력
if st.button("🎲 이름 생성하기"):
    name = random.choice(mood_playlists[mood])
    st.markdown(f'<div class="playlist">✨ 추천 이름: <br><strong>{name}</strong></div>', unsafe_allow_html=True)
    st.code(name, language="text")

    # 클립보드 복사 안내
    st.caption("⬆️ 위 텍스트를 복사해서 사용해보세요!")



if st.button("이름 생성하기"):
    playlist_name = random.choice(mood_playlists[mood])
    st.success(f"✨ 추천 플레이리스트 이름: **{playlist_name}**")

