import math

T = int(input())


for _ in range(T):
    num = int(input())

    x = math.sqrt(num)
    print(2 * (math.floor(x) + math.ceil(num / math.floor(x))))

