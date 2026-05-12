data = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp
            for i in range(len(data)):
                print(data[i], end=' ')
            print()

    if data == answer:
        break