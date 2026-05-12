from transformers import BertTokenizer, BertModel
import torch

# 임베딩할 단어 리스트
categories = ['fruit', 'vehicle', 'animal', 'tool', 'electronic device', 'sport', 'profession', 'emotion', 'planet', 'musical instrument']

# BERT 모델 및 토크나이저 불러오기
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 단어 임베딩 벡터를 저장할 리스트
embedding_vectors = []

# 각 단어를 임베딩 벡터로 변환하고 embedding_vectors에 저장
for word in categories:
    # TODO: 여기에 코드를 작성하세요
    
# 각 단어의 임베딩 벡터 출력
for word, vec in zip(categories, embedding_vectors):
    print(f"{word} 임베딩 벡터: {vec}")