import streamlit as st
import random
import re

# 초성 리스트
chosung_map = {
    "ㄱ": ["끝을 보는 집중력", "강철 같은 끈기", "고요 속의 추진력"],
    "ㄴ": ["늘 새로운 시도", "나직한 자신감", "능청스러운 매력"],
    "ㄷ": ["단단한 신념", "독특한 시선", "도도한 기품"],
    "ㄹ": ["리듬감 있는 사고", "라이벌을 넘는 열정", "러블리한 에너지"],
    "ㅁ": ["마음을 울리는 진심", "매력 넘치는 감성", "묵직한 신뢰감"],
    "ㅂ": ["변화를 두려워하지 않는 용기", "바다 같은 포용력", "반짝이는 아이디어"],
    "ㅅ": ["스스로를 믿는 자신감", "신중한 판단력", "새벽 같은 집중력"],
    "ㅇ": ["온화한 카리스마", "의연한 자세", "영감 넘치는 감성"],
    "ㅈ": ["자기 주도적 삶", "진지한 끌림", "작지만 강한 존재감"],
    "ㅊ": ["차분한 카리스마", "치밀한 전략가", "청량한 감성"],
    "ㅋ": ["쿨한 이성", "카리스마 폭발", "키득이는 유머감각"],
    "ㅌ": ["타인을 배려하는 마음", "탁월한 선택력", "트렌디한 감각"],
    "ㅍ": ["파워풀한 열정", "평화를 중시하는 태도", "포근한 인상"],
    "ㅎ": ["한결같은 사람", "혼자서도 잘 해내는 독립성", "화사한 분위기"],
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

