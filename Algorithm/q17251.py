N = int(input())
data = list(map(int, input().split()))

max_value, left, right = 0, 0, 0

for i in range(N):
    if data[i] > max_value:
        max_value = data[i]
        left = i
        right = i
    elif data[i] == max_value:
        right = i

left_length = left
right_length = N - 1 - right

if left_length > right_length:
    print('B')
elif right_length > left_length:
    print('R')
else:
    print('X')