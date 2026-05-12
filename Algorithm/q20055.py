N, K = map(int, input().split())
A = list(map(int, input().split()))

robot = [False] * N
result = 0

while True:
    result += 1

    # 1. rotate belt and robot (A도 slicing으로 회전)
    A = [A[-1]] + A[:-1]
    robot = [False] + robot[:-1]
    robot[-1] = False

    # 2. move the robots
    for i in range(N - 1):
        idx = N-2-i
        if robot[idx] and not robot[idx + 1] and A[idx + 1] > 0:
            robot[idx] = False
            robot[idx + 1] = True
            A[idx + 1] -= 1
    robot[-1] = False

    # 3. put robot
    if A[0] > 0 and not robot[0]:
        robot[0] = True
        A[0] -= 1

    # 4. check belt
    if A.count(0) >= K:
        break

print(result)
