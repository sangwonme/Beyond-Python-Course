from openai import OpenAI
client = OpenAI(api_key=YOUR_KEY_HERE)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
  
)

print(completion.choices[0].message)

import pdb; pdb.set_trace()