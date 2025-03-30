from openai import OpenAI

# OpenAI 클라이언트 설정
client = OpenAI(api_key=YOUR_KEY_HERE)

# 과일 가격
prices = {
    "바나나": 1000,
    "사과": 2000,
    "복숭아": 3000,
    "포도": 2500,
    "오렌지": 1500,
    "수박": 12000,
    "자두": 1800,
    "배": 2200,
    "귤": 800,
    "딸기": 4500,
    "체리": 5000,
    "키위": 2000,
    "파인애플": 7000,
    "망고": 6500,
}

answers = [38000, 36000, 14700, 32300, 56000]

# 테스트 케이스
shopping_stories = [
    '''
    용식이는 바나나를 5개를 사려다가 생각해보니 1개만 있으면 충분할 것 같아서 1개만 사고 나머지 4개는 그냥 내려두었다. 
    사과는 총 10개가 있었는데 그 중에서 절반 만큼을 구매했다.
    복숭아는 구매하지 않은 바나나와 사과의 개수만큼 구매했다. 
    '''
    ,
    '''
    규리는 포도를 12송이 사려다가 너무 많을 것 같아서 3분의 2만 구매했다. 
    사과는 처음에 4개를 사려고 했는데, 마침 1+1 행사가 있어 2개만 가격을 내고 4개를 가져갔다. 
    수박은 너무 무거워서 안 사기로 했고, 대신 복숭아를 사과의 개수만큼 샀다.
    '''
    ,
    '''
    지혜는 바나나를 3개, 사과를 2개, 그리고 자두를 5개 담았지만, 계산대 앞에서 자두가 너무 비싸다는 것을 깨닫고 2개만 남기고 나머지는 내려두었다. 
    계산 중 점원이 배를 추천해서 배 2개를 추가했고, 바나나 가격이 10% 할인 중이라 할인된 가격으로 계산되었다.
    '''
    ,
    '''
    철수는 귤 10개를 사기로 마음먹었지만 4개는 상한 걸 발견해서 다시 내려놓았다. 
    딸기는 총 6팩 중에서 3팩만 상태가 좋아서 그것만 샀고, 복숭아는 사려던 사과의 개수와 같은 수만큼 구매했다. 
    사과는 총 4개를 사려했지만 마지막에는 그 중 1개만 골랐다. 
    '''
    ,
    '''
    민지는 체리를 사러 갔지만 재고가 8팩밖에 없었다. 원래 10팩을 사려 했지만 8팩을 모두 구매했고, 키위는 5개를 사려고 했으나 예산이 부족해 3개만 구매했다. 
    대신 파인애플 1개를 추가로 샀고, 처음에 사려던 망고는 너무 비싸 포기했다. 대신 복숭아를 망고의 개수만큼 샀다. 
    '''
]

correct = 0

# Test for each test case
for i in range(len(shopping_stories)):
    
    # Testcase
    shopping_story = shopping_stories[i]
    print(f'Test Case {i+1}: {shopping_story}')

    # TODO: Update prompts!
    prompt = f'''
    Answer how many fruits
    {prices}
    {shopping_story}
    '''

    # GPT API
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
      ]
    )

    # GPT Result
    response = completion.choices[0].message.content
    print('--- GPT Response: ')
    print(response)

    # Upate answer
    answer = 0 #TODO: Update the answer

    # Count correct
    passed = False
    if type(answer) == int:
        if answer == answers[i]:
            correct += 1
            passed = True
    print(f'Test Case {i+1}: Correct!' if passed else f'Test Case {i+1}: Failed...')
    print('='*30)


# Show result
print(f"\n Result: {correct} / {len(shopping_stories)} Correct")
if correct == len(shopping_stories):
    print("All test cases passed! Congratulations!")
else:
    print("Try refining your prompts to improve accuracy.")