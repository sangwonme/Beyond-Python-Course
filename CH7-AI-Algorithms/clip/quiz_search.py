import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from torch.nn.functional import cosine_similarity
import os
import numpy as np

text_embedding = torch.zeros(0)
image_embeddings = torch.zeros(0)

# CLIP 모델 불러오기
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 이미지 불러오기
image_filenames = [] # 이미지 파일 경로 200개를 저장
images = [] # 이미지 객체 200개를 저장

for i in range(200):
    pass
    # 이미지 파일 경로를 파악하여 image_filenames 생성
    # TODO: 퀴즈 3 - 여기에 코드를 작성하시오.

for i in range(len(image_filenames)):
    image = Image.open(image_filenames[i])
    images.append(image)

print(f'Total {len(images)} images are loaded!')

# 이미지 임베딩
# TODO: 퀴즈 4 - 여기에 코드를 작성하시오.

print(f'Image Embedding\'s shape: {image_embeddings.shape}')

# Top-1 이미지 검색 함수
def search_image_by_text(text_prompt):
    # 텍스트 임베딩
    # TODO: 퀴즈 5 - 여기에 코드를 작성하시오.

    print(f'Text Embedding\'s shape: {text_embedding.shape}')

    # 코사인 유사도
    similarities = cosine_similarity(text_embedding, image_embeddings)
    print('-----------------------------------------------------')
    print("The most similar image found is: ", end='')
    # TODO: 퀴즈 6 - 여기에 코드를 작성하시오.


# -------------------------------------------------
# 사용자 입력: 사용자 입력이 'exit'이면 프로그램 종료
while True:
    text_prompt = input("Enter a description for the image search: ")
    if text_prompt == 'exit':
        break
    search_image_by_text(text_prompt)
    