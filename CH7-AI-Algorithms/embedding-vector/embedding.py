from transformers import BertTokenizer, BertModel
import torch

# BERT 토크나이저와 모델 불러오기
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 문장 정의
sentence = "I love reading books."

# 문장을 토큰으로 변환 및 BERT 입력 형식으로 변환
inputs = tokenizer(sentence, return_tensors='pt')

# BERT 모델을 통해 임베딩 벡터 얻기
with torch.no_grad():
    outputs = model(**inputs)

# 임베딩 벡터 추출
embedding_vector = outputs.last_hidden_state.mean(dim=1)
print("임베딩 벡터:", embedding_vector)
