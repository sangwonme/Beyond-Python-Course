from collections import deque

N, M = map(int, input().split())

# Graph
graph = []
for _ in range(N):
    row = list(map(int, list(input())))
    graph.append(row)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# Visited
visited = [[False for _ in range(M)] for _ in range(N)]

# Queue
sx, sy = 0, 0
distance = 1
queue = [(sx, sy, distance)]
queue = deque(queue)
visited[sx][sy] = True

# BFS
while queue:
    cx, cy, cur_dist = queue.popleft()
    # end
    if cx == N-1 and cy == M-1:
        print(cur_dist)
        break
    # neighbor queueing
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        # boundary check
        if 0 <= nx < N and 0 <= ny < M:
            # path check
            if graph[nx][ny] == 1:
                # visited check
                if not visited[nx][ny]:
                    queue.append((nx, ny, cur_dist + 1))
                    visited[nx][ny] = True