import numpy as np
from transformers import BertTokenizer, BertModel
import torch

# 코사인 유사도 함수 정의
def cosine_similarity(vec1, vec2):
    # TODO: 퀴즈 1 정답 입력
    pass

# 임베딩할 단어 리스트
categories = ['fruit', 'vehicle', 'animal', 'tool', 'electronic device', 'sport', 'profession', 'emotion', 'planet', 'musical_instrument']

# BERT 모델 및 토크나이저 불러오기
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 단어 임베딩 벡터를 저장할 리스트
embedding_vectors = []

# 각 단어를 임베딩 벡터로 변환하고 embedding_vectors에 저장
for word in categories:
    # TODO: 퀴즈 2 정답 입력

# 사용자 입력 받기
user_input = input("텍스트를 입력하세요: ")

# 입력된 단어(user_input)를 임베딩 벡터로 변환
# TODO: 여기에 코드를 작성하게요.

# 코사인 유사도를 통해 입력된 단어와 각 카테고리의 유사도 계산
similarities = []
# TODO: 여기에 코드를 작성하세요.

# 유사도가 가장 높은 카테고리 선택
max_index = np.argmax(similarities)
predicted_category = categories[max_index]

# 결과 출력
print(f"입력한 단어 '{user_input}'는 '{predicted_category}' 카테고리와 가장 유사합니다.")
print('유사도 결과')
for i in range(len(categories)):
    print(f'- {categories[i]}: {similarities[i]}' )