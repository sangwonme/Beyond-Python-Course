import torch
import numpy as np
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load Pre-trained BERT Model and Tokenizer
# This might take a moment to download on the first run
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embedding(text):
    """Encodes text into a BERT vector (768 dimensions)"""
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the mean of the last hidden states as the sentence embedding
    return outputs.last_hidden_state.mean(dim=1).numpy()

# 2. Support Database (Knowledge Base)
support_db = [
    {
        "topic": "Shipping",
        "review_text": "The package hasn't arrived yet. Please check shipping.",
        "support_response": "We apologize for the delay. We are checking your tracking information right now."
    },
    {
        "topic": "Quality",
        "review_text": "The product quality is very different from the picture.",
        "support_response": "We are sorry to hear that. You can request a return or exchange through our website."
    },
    {
        "topic": "Size",
        "review_text": "The design is pretty but the size is a bit small.",
        "support_response": "Thank you for your feedback! Please refer to our size guide for your next purchase."
    }
]

# 3. Pre-calculate Embeddings for the Database
print("Embedding database... please wait.")
db_texts = [item['review_text'] for item in support_db]
# Concatenate all embeddings into one matrix
db_matrix = np.vstack([get_bert_embedding(text) for text in db_texts])

# 4. Process New Inquiry
query_text = "My order is taking too long. Where is my stuff?"
query_vec = get_bert_embedding(query_text)

# 5. Calculate Similarity
# Result shape: (1, 3)
similarities = cosine_similarity(query_vec, db_matrix)[0]

# 6. Find and Display the Best Support Response
best_idx = np.argmax(similarities)
confidence = similarities[best_idx]
matched_item = support_db[best_idx]

print("\n" + "="*50)
print(f"Customer Inquiry: {query_text}")
print(f"Detected Topic: {matched_item['topic']}")
print(f"Similarity Score: {confidence:.4f}")
print("-" * 50)
print(f"Suggested Support Response:")
print(f">> {matched_item['support_response']}")
print("="*50)