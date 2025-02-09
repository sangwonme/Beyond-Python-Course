# input
T = int(input())
for _ in range(T):
    # command input
    command = input()
    # init
    dirs = [[0,1], [-1,0], [0,-1], [1,0]]
    dir_idx = 0
    pos = [0,0]
    x_min, x_max, y_min, y_max = 0, 0, 0, 0
    # simulate for every command
    for com in command:
        if com == 'F':
            pos[0] += dirs[dir_idx][0]
            pos[1] += dirs[dir_idx][1]
        elif com == 'B':
            pos[0] -= dirs[dir_idx][0]
            pos[1] -= dirs[dir_idx][1]
        elif com == 'L':
            dir_idx = (dir_idx + 1) % 4
        elif com == 'R':
            dir_idx = (dir_idx - 1) % 4
        # update min / max
        if pos[0] < x_min:
            x_min = pos[0]
        if pos[0] > x_max:
            x_max = pos[0]
        if pos[1] < y_min:
            y_min = pos[1]
        if pos[1] > y_max:
            y_max = pos[1]
    # print area
    print((x_max - x_min) * (y_max - y_min))
