import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from torch.nn.functional import cosine_similarity
import os
import numpy as np

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Directory containing images
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(current_dir, 'search-image')

# Load images from the directory and preprocess them
images = []
image_filenames = []

for filename in os.listdir(image_dir):
    if filename.endswith(".JPEG") or filename.endswith(".png") or filename.endswith('.jpg'):
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)
        images.append(image)
        image_filenames.append(filename)

# Encode images with CLIP
image_inputs = processor(images=images, return_tensors="pt", padding=True)
with torch.no_grad():
    image_embeddings = model.get_image_features(**image_inputs)

# Function to search images based on text prompt
def search_image_by_text(text_prompt):
    # Encode the text prompt
    text_inputs = processor(text=[text_prompt], return_tensors="pt", padding=True)
    with torch.no_grad():
        text_embedding = model.get_text_features(**text_inputs)

    # Calculate cosine similarity
    similarities = cosine_similarity(text_embedding, image_embeddings)
    best_match_idx = similarities.argmax().item()

    import pdb; pdb.set_trace()

    print(f"The most similar image found is: {image_filenames[best_match_idx]}")

# Prompt user for a description and search
text_prompt = input("Enter a description for the image search: ")
search_image_by_text(text_prompt)
