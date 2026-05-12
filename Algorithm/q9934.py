n = int(input())
arr = list(map(int, input().split()))

graph = [[] for _ in range(n)]
depth = 0

def maketree(start, end, depth):
    if start >= end : return 

    mid = (start + end) // 2

    maketree(start, mid, depth + 1)
    graph[depth].append(arr[mid])
    maketree(mid + 1, end, depth + 1)

maketree(0, 2 ** n - 1, depth)
for i in range(n):
    for j in range(len(graph[i])):
        print(graph[i][j])