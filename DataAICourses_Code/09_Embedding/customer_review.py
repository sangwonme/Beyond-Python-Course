import torch
import numpy as np
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load Pre-trained BERT Model and Tokenizer
# This might take a moment to download on the first run
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embedding(text):
    # TODO: Return BERT Embedding with given text

    return # TODO: Change Return

# 2. Support Database (Knowledge Base)
previous_reviews = [
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
db_texts = [item['review_text'] for item in previous_reviews]
# Concatenate all embeddings into one matrix
db_matrix = np.vstack([get_bert_embedding(text) for text in db_texts])

# 4. Process New Inquiry
new_review = "My order is taking too long. Where is my stuff?"
query_vec = None # TODO: Update query_vec as embedding of new_review

# 5. Calculate Similarity
similarities = None # TODO: Update similarities as cosine similarity between new_review and db_matrix

# 6. Find and Display the Best Support Response
best_idx = None # TODO: Update best_idx as the index of db_matrix where the cosine similarity is the highest (study & use .argmax() function)
confidence = similarities[best_idx]
matched_item = previous_reviews[best_idx]

print("\n" + "="*50)
print(f"Customer Inquiry: {new_review}")
print(f"Detected Topic: {matched_item['topic']}")
print(f"Similarity Score: {confidence:.4f}")
print("-" * 50)
print(f"Suggested Support Response:")
print(f">> {matched_item['support_response']}")
print("="*50)