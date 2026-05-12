N = int(input())
S = input()

# init
max_size = 0 # measure the max_size of the stack
stack = []

# stack operation
for c in S:
    # if popable -> pop
    if len(stack) > 0 and stack[-1] != c:
        stack.pop()
    # else -> push and update max_size
    else:
        stack.append(c)
        if max_size < len(stack):
            max_size = len(stack)

# if valid
if len(stack) == 0:
    print(max_size)
else:
    print(-1)