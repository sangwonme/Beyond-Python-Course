import base64
from openai import OpenAI

# Load and encode the image
image_path = './data/image.png'
with open(image_path, 'rb') as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the image content for the message
image_message = {
    "type": "image_url",
    "image_url": {
        "url": f"data:image/png;base64,{base64_image}"
    }
}

# Create the client
client = OpenAI()

# Send a message that includes both text and image
completion = client.chat.completions.create(
    model="gpt-4o",  # or "gpt-4-vision-preview"
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image."},
                image_message
            ]
        }
    ],
    max_tokens=300
)

print(completion.choices[0].message.content)
