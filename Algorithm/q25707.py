N = int(input())
data = list(map(int, input().split()))

data.sort()

print(2*(data[-1]-data[0]))