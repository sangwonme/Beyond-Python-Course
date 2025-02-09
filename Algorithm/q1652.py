
N = int(input())
data = []
for _ in range(N):
    data.append(input())

# horizontal
horizontal = 0
for i in range(N):
    space = 0
    for j in range(N):
        if data[i][j] == '.':
            space += 1
        else:
            space = 0

        if space == 2:
            horizontal += 1

# horizontal
vertical = 0
for j in range(N):
    space = 0
    for i in range(N):
        if data[i][j] == '.':
            space += 1
        else:
            space = 0

        if space == 2:
            vertical += 1

print(horizontal, vertical)

# x = int(input())
# a = [] 
# b = []
# for i in range(x):
#     a.append([])
#     y = input()
#     for j in range(x):
#         a[i].append(y[j])
# for i in range(x):
#     b.append([])
#     for j in range(x):
#         b[i].append(a[j][i])


# xcnt = 0
# ycnt = 0

# for i in range(x):
#     cnt = 0
#     for j in range(x):
#         if a[i][j] == ".":
#             cnt += 1
#         elif a[i][j] == "X":
#             cnt = 0
#         if cnt == 2:
#             xcnt += 1

# for i in range(x):
#     cnt = 0
#     for j in range(x):
#         if b[i][j] == ".":
#             cnt += 1
#         elif b[i][j] == "X":
#             cnt = 0
#         if cnt == 2:
#             ycnt += 1

# print(f"{xcnt} {ycnt}")