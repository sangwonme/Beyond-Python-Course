import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from torch.nn.functional import cosine_similarity
import os
import numpy as np

# CLIP 모델 불러오기
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 이미지 불러오기
images = []
image_filenames = []
for i in range(9):
    image_filenames.append('./topk-image/dog_'+str(i)+'.png')
    images.append(Image.open(image_filenames[i]))

# 이미지 임베딩
image_inputs = processor(images=images, return_tensors="pt", padding=True)
with torch.no_grad():
    image_embeddings = model.get_image_features(**image_inputs)

# 텍스트
text = ['A dog is eating food']
text_inputs = processor(text=text, return_tensors="pt", padding=True)
with torch.no_grad():
    text_embedding = model.get_text_features(**text_inputs)

# 코사인 유사도
similarities = cosine_similarity(text_embedding, image_embeddings)

# TOP-K 결과 찾기
k = 3
top_3_indices = similarities.topk(k).indices
print("Top 3 most similar images:")
for idx in top_3_indices:
    print(f"- {image_filenames[idx]}")
