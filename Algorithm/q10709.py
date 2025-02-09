# input
H, W = map(int, input().split())
data = []
for i in range(H):
    data.append(input())

# init -1
ouput = []
for i in range(H):
    line = []
    for j in range(W):
        line.append(-1)
    ouput.append(line)


for i in range(H):
    cloud_found = False
    # 이 줄에서 구름이 있었다면 num += 1 / 구름을 새로 찾으면 -1 대입
    for j in range(W):
        if data[i][j] == 'c':
            cloud_found = True
            num = -1
        
        if cloud_found:
            num += 1
            ouput[i][j] = num

for i in range(H):
    for j in range(W):
        print(ouput[i][j], end= ' ')
    print()