N, M = map(int, input().split())

# input
data = []
for _ in range(N):
    data.append(input())

ans = ''

# left / right idx
left = -1
right = -1
for i in range(N):
    for j in range(M):
        if left == -1 and data[i][j] == '#':
            left = j
        if left != -1 and data[i][j] == '#':
            right = j
    if left != -1 and right != -1:
        break

# iterate in rows
for i in range(N):
    for j in range(M):
        # check up / down
        if j < M-3 and data[i][j:j+3] == '#.#':
            if i > 0 and data[i-1][left] == '#':
                ans = 'DOWN'
            else:
                ans = 'UP'
        # check left / right
        if data[i][left] == '#' and data[i][right] == '.':
            ans = 'RIGHT'
        elif data[i][left] == '.' and data[i][right] == '#':
            ans = 'LEFT'

print(ans)
        