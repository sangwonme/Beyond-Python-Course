from openai import OpenAI

client = OpenAI(api_key=YOUR_KEY_HERE)

# 대화 내역 리스트
chat_history = [{"role": "developer", "content": "You are a helpful chat-bot."}]

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("대화를 종료합니다.")
        break

    # 사용자 입력 추가
    chat_history.append({"role": "user", "content": user_input})

    # OpenAI API 요청
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history
    )

    # 챗봇 응답 추가 및 출력
    assistant_message = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": assistant_message})

    print("\nGPT: " + assistant_message)
