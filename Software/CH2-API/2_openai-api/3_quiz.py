import streamlit as st
from openai import OpenAI

# OpenAI 클라이언트 설정
client = OpenAI(api_key=YOUR_KEY_HERE)

st.title("AI Chatbot with Token Tracker")

# Session State 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": "You are a helpful chatbot."}]

if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

# 토큰 사용량을 표시하는 상단 영역
st.markdown(f"### :rocket: Total Tokens Used: **{st.session_state.total_tokens}**")

# 사용자 입력 받기
user_input = st.text_input("You:", key="user_input")

if st.button("Send") and user_input != "":
    # 사용자 메시지를 대화 내역에 추가
    # TODO

    # OpenAI API 요청
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.chat_history
    )

    # 사용된 토큰을 누적
    # TODO

    # 응답 대화내역에 저장
    # TODO

    # UI 업데이트
    st.experimental_rerun()

# 채팅 내역 출력
container = st.container(border=True)
with container:
  for msg in st.session_state.chat_history:
      if msg["role"] == "user":
          container.write(f"**You:** {msg['content']}")
      elif msg["role"] == "assistant":
          container.write(f"**GPT:** {msg['content']}")
