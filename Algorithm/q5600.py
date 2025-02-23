A, B, C = map(int, input().split())
N = int(input())

test = []
for _ in range(N):
    test.append(list(map(int, input().split())))

# Initiate result with unknown state (2) - 1 indexing
result = [2] * (A+B+C+1)

# Check the well-working
for i in range(N):
    if test[i][3] == 1:
        for j in range(3):
            result[test[i][j]] = 1

# Check if there are brokens
for i in range(N):
    if test[i][3] == 0:
        # If there are 2 working, then remaining one is broken
        cnt = 0
        broken = -1
        for j in range(3):
            if result[test[i][j]] == 2:
                broken = test[i][j]
            if result[test[i][j]] == 1:
                cnt += 1
        if cnt == 2:
            result[broken] = 0

for i in range(1, A+B+C+1):
    print(result[i])