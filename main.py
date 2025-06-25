import streamlit as st
from datetime import datetime

st.title("📅 지금 몇 시지?")

now = datetime.now()
st.write("현재 날짜와 시간:")
st.write(now.strftime("%Y-%m-%d %H:%M:%S"))
