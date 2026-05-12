from openai import OpenAI

from openai import OpenAI

client = OpenAI(api_key=YOUR_KEY_HERE)

audio_file = open("./data/audio.wav", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

# 변환된 텍스트를 파일로 저장
with open("./output/transcription.txt", "w") as text_file:
    text_file.write(transcription.text)

print("Transcription saved to transcription.txt")