import base64

# 이미지 파일을 base64 문자열로 인코딩
with open("./image/apple.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

print(base64_image)  # 문자열의 앞부분만 출력