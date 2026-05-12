import requests

url = "https://api.sunoapi.org/api/v1/generate"

payload = {
    "prompt": "A calm and relaxing piano track with soft melodies",
    "style": "Classical",
    "title": "Peaceful Piano Meditation",
    "customMode": True,
    "instrumental": True,
    "model": "V3_5",
    "negativeTags": "Heavy Metal, Upbeat Drums",
    "callBackUrl": "https://api.example.com/callback"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())