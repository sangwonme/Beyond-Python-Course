from openai import OpenAI
client = OpenAI(api_key=YOUR_KEY_HERE)

audio_file= open("./data/jackhammer.wav", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)