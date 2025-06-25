import streamlit as st
import random

st.title("✊✋✌️ 가위바위보 게임")

user = st.selectbox("당신의 선택은?", ["가위", "바위", "보"])
if st.button("결과 보기"):
    comp = random.choice(["가위", "바위", "보"])
    st.write(f"컴퓨터의 선택: {comp}")

    if user == comp:
        st.success("무승부!")
    elif (user == "가위" and comp == "보") or \
         (user == "바위" and comp == "가위") or \
         (user == "보" and comp == "바위"):
        st.success("당신이 이겼습니다!")
    else:
        st.error("졌습니다 ㅠㅠ")
