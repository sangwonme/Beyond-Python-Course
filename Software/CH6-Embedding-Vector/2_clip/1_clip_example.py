import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import os
import numpy as np

# 코사인 유사도 계산
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

# CLIP 모델 불러오기
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 이미지 불러오기
image = Image.open('./cat.jpg')

# 이미지 임베딩하기
image_inputs = processor(images=image, return_tensors="pt", padding=True)
with torch.no_grad():
    image_embedding = model.get_image_features(**image_inputs)

# 텍스트 정의
texts = ['A dog', 'A cat', 'A nuclear submarine']

# 각 텍스트 임베딩하기
text_inputs = processor(text=texts, return_tensors="pt", padding=True)
with torch.no_grad():
    text_embedding = model.get_text_features(**text_inputs)

# 각 텍스트의 코사인 유사도 계산
print('=======================================')
for i in range(len(texts)):
    similarity = cosine_similarity(image_embedding[0], text_embedding[i])
    print(texts[i], ' : ', similarity)
print('=======================================')
