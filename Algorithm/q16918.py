R, C, N = map(int, input().split())

# input
data = []
for _ in range(R):
    data.append(list(input()))

# init time
time = []
for i in range(R):
    row = []
    for j in range(C):
        if data[i][j] == '.':
            row.append(0)
        elif data[i][j] == 'O':
            row.append(2)
    time.append(row)

# direction
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# simulation
for n in range(N-1):
    explosion = []
    for i in range(R):
        for j in range(C):
            # case time = 1 -> set bomb = increase time
            # case time = 2 -> increase time
            if time[i][j] <= 2:
                time[i][j] += 1
            # case time = 3 -> set 0 / set adj as 0
            elif time[i][j] == 3:
                time[i][j] = 0
                for k in range(4):
                    if 0 <= i+dx[k] < R and 0 <= j+dy[k] < C:
                        explosion.append([i+dx[k], j+dy[k]]) # seperate explosion to ensure all bombs to be exploded (not removed)
            
    # explode
    for i in range(len(explosion)):
        x = explosion[i][0]
        y = explosion[i][1]
        time[x][y] = 0

# print
for i in range(R):
    for j in range(C):
        if time[i][j] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print()