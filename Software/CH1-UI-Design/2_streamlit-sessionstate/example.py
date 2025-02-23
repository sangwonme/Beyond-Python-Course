import streamlit as st

st.title("Counter without Session State")

count = 0  # 매번 실행될 때마다 count가 초기화됨
if st.button("Increase"):
    count += 10
st.write("Count:", count)