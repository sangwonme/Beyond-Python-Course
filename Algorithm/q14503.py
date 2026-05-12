# input
N, M = map(int, input().split())
r, c, d = map(int, input().split())

# input
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

# directions
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# clean
clean = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(False)
    clean.append(row)

# ans
cnt = 0

# simulate
y = r
x = c
dir = d
while True:
    # print('------------------')
    # print('Y, X: ', y, x)
    # for i in range(N):
    #     for j in range(M):
    #         print(int(clean[i][j]), end = ' ')
    #     print()

    # Step 1: Not clean -> clean
    if not clean[y][x]:
        clean[y][x] = True
        cnt += 1
    
    # Step 2: Check Adj
    neighbor_all_clean = True
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < N and 0 <= nx < M and data[ny][nx] == 0 and not clean[ny][nx]:
            neighbor_all_clean = False
    # Case 1: All clean
    if neighbor_all_clean:
        ny = y - dy[dir]
        nx = x - dx[dir]
        # If movable -> move
        if 0 <= ny < N and 0 <= nx < M and data[ny][nx] == 0:
            y = ny
            x = nx
        # If not movable -> break
        else:
            break
    # Case 2: Not all clean
    else:
        # Rotate
        dir = (dir - 1) % 4
        # If front is not clean -> move front
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= ny < N and 0 <= nx < M and data[ny][nx] == 0 and not clean[ny][nx]:
            y = ny
            x = nx
    
print(cnt)