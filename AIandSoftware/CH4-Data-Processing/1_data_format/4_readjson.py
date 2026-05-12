import json

# JSON 파일 열기
with open('./data/people.json', 'r') as f:
    data = json.load(f)

print(data)
print(data[0])
print(data[0]['name'])
print(data[0]['addresses'][0]['type'])