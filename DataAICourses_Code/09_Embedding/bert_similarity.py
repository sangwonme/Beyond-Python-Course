import torch
import numpy as np
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_embedding(text):
    # Tokenize and convert to tensor
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the mean of the last hidden state as the sentence/word embedding
    return outputs.last_hidden_state.mean(dim=1)

# 2. Define the words
target = "apple"
candidates = ["pear", "banana", "mango", "orange", "strawberry", "dog", "nuclear submarine"]

# 3. Calculate embeddings
target_vec = get_embedding(target)
candidate_vecs = torch.cat([get_embedding(word) for word in candidates])

# 4. Compute cosine similarity
# Result is a 2D array, we take the first row [0]
similarities = cosine_similarity(target_vec, candidate_vecs)[0]

# 5. Identify the best similarity
best_index = np.argmax(similarities)
best_word = candidates[best_index]
confidence = similarities[best_index]


# 6. Output results
print(f"BERT Cosine Similarity with '{target}':\n")
for word, score in zip(candidates, similarities):
    print(f"{word:18}: {score:.4f}")

print("-" * 30)
print(f"Best Match: '{best_word}' with a score of {confidence:.4f}")