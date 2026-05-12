from collections import deque

T = int(input())

# direction of knight
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

# Print answer for each test cases
for test_case in range(T):
  l = int(input())
  # visited matrix
  visited = [[False for i in range(l)] for j in range(l)]
  # init input
  start = list(map(int, input().split()))
  end = list(map(int, input().split()))
  # queue setup
  x, y = start
  queue = deque([start])
  visited[x][y] = True
  distance = 0
  # bfs
  while queue:
    for tmp in range(len(queue)):
      x, y = queue.popleft()
      # end
      if [x, y] == end:
        print(distance)
        break
      # check all neighbors
      for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        # boundary check
        if 0 <= nx < l and 0 <= ny < l:
            # visit
            if not visited[nx][ny]:
              queue.append([nx, ny])
              visited[nx][ny] = True
    # add distance when chunk is done
    distance += 1