# input
M, n = map(int, input().split())

# init
dirs = [[1,0], [0,1], [-1,0], [0,-1]]
dir_idx = 0
pos = [0, 0]
valid = True

# repeat n times
for i in range(n):
    command = input().split()
    if command[0] == 'MOVE':
        pos[0] += (int(command[1]) * dirs[dir_idx][0])
        pos[1] += (int(command[1]) * dirs[dir_idx][1])
    elif command[0] == 'TURN':
        if int(command[1]) == 0:
            dir_idx = (dir_idx + 1) % 4
        elif int(command[1]) == 1:
            dir_idx = (dir_idx - 1) % 4
    # valid check
    if not(0 <= pos[0] <= M and 0 <= pos[1] <= M):
        valid = False

# print answer
if valid:
    print(pos[0], pos[1])
else:
    print(-1)
