# input
king, dol, N = input().split()
N = int(N)
commands = []
for _ in range(N):
    commands.append(input())

# directions and command type
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
command_type = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

# convert corrdinate
king_x = ord(king[0]) - ord('A')
king_y = int(king[1]) - 1
dol_x = ord(dol[0]) - ord('A')
dol_y = int(dol[1]) - 1

# move
for command in commands:
    # get dx dy
    idx = 0
    for i in range(len(command_type)):
        if command_type[i] == command:
            idx = i
    
    # nx, ny
    king_nx = king_x + dx[idx]
    king_ny = king_y + dy[idx]
    dol_nx = dol_x
    dol_ny = dol_y
    if king_nx == dol_x and king_ny == dol_y:
        dol_nx += dx[idx]
        dol_ny += dy[idx]

    # if movable -> move
    if 0 <= king_nx < 8 and 0 <= king_ny < 8 and 0 <= dol_nx < 8 and 0 <= dol_ny < 8:
        king_x = king_nx
        king_y = king_ny
        dol_x = dol_nx
        dol_y = dol_ny

# convert cordinate
print(chr(king_x + ord('A')) + str(king_y+1))
print(chr(dol_x + ord('A')) + str(dol_y+1))