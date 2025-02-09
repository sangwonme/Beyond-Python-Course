T = int(input())
for _ in range(T):
    data = input()

    ans = 'YES'

    cnt = 0
    for char in data:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
            if cnt < 0:
                ans = 'NO'
                break
    
    if cnt != 0:
        ans = 'NO'

    print(ans)