import streamlit as st
import random

# 기분별 플레이리스트 이름 후보
mood_playlists = {
    "행복": [
        "햇살 속에 걷는 기분",
        "레몬소다 댄스파티",
        "구름 위를 걷는 듯",
        "기분 좋은 알람",
        "웃음이 번지는 오후"
    ],
    "슬픔": [
        "비 오는 창가에서",
        "조용한 눈물의 선율",
        "회색 하늘과 나",
        "마음의 쉼표",
        "조용한 방, 나 혼자"
    ],
    "화남": [
        "속이 뻥 뚫리는 사운드",
        "드럼과 분노",
        "불꽃 튀는 베이스",
        "소리 지르고 싶은 밤",
        "분노의 질주"
    ],
    "집중": [
        "코딩 집중 모드",
        "한 줄 한 줄 깊게",
        "생산성 200% 트랙",
        "조용한 몰입의 시간",
        "Deep Focus Zone"
    ],
    "설렘": [
        "심장이 두근두근",
        "첫눈 오는 날의 감성",
        "너와 나, 설레는 시작",
        "고백 5초 전",
        "커피향과 눈맞춤"
    ]
}

# Streamlit UI
st.title("🎧 기분 기반 플레이리스트 이름 생성기")
st.markdown("당신의 현재 기분은 어떤가요? 그 기분에 어울리는 플레이리스트 이름을 추천해드릴게요!")

mood = st.selectbox("기분을 선택하세요", list(mood_playlists.keys()))

if st.button("이름 생성하기"):
    playlist_name = random.choice(mood_playlists[mood])
    st.success(f"✨ 추천 플레이리스트 이름: **{playlist_name}**")

}

# 초성 추출 함수
def get_chosung(text):
    def decompose(char):
        if re.match(r"[가-힣]", char):
            code = ord(char) - 44032
            cho = code // (21 * 28)
            return chr(0x3131 + cho)  # 초성 유니코드 범위 (ㄱ~ㅎ)
        return char
    return [decompose(c) for c in text if re.match(r"[가-힣]", c)]

# UI
st.title("🧠 초성 기반 이름 해석기")

name = st.text_input("이름을 입력하세요 (예: 민수, 지훈, 하늘)")

if st.button("초성 해석하기"):
    if not name.strip():
        st.warning("이름을 입력해주세요!")
    else:
        chosungs = get_chosung(name)
        st.markdown("### 🪄 해석 결과")
        for ch in chosungs:
            meaning = random.choice(chosung_map.get(ch, [f"{ch}는 특별한 힘을 지녔어요!"]))
            st.write(f"**{ch}** → {meaning}") 

