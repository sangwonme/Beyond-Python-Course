import os
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Directory containing images, and labels dictionary
image_dir = "path_to_your_images"  # Update this with your image directory path
labels_dict = {
    "cat": 0,
    "dog": 1
    # Add other classes as needed
}

# Prepare images and labels
images = []
labels = []

for label_name, label_id in labels_dict.items():
    class_dir = os.path.join(image_dir, label_name)
    for filename in os.listdir(class_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(class_dir, filename)
            images.append(Image.open(image_path))
            labels.append(label_id)

# Extract CLIP embeddings for each image
image_inputs = processor(images=images, return_tensors="pt", padding=True)
with torch.no_grad():
    image_embeddings = model.get_image_features(**image_inputs)
    image_embeddings = image_embeddings / image_embeddings.norm(dim=-1, keepdim=True)  # Normalize embeddings

# Convert embeddings to a NumPy array
image_embeddings_np = image_embeddings.cpu().numpy()
labels_np = torch.tensor(labels).cpu().numpy()

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(image_embeddings_np, labels_np, test_size=0.2, random_state=42)

# Initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)  # You can adjust the number of neighbors as needed

# Train the KNN classifier
knn.fit(X_train, y_train)

# Predict on the test set
y_pred = knn.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Test set accuracy: {accuracy * 100:.2f}%")
