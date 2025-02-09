N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Search A[0]'s pos in B
pos = 0
for i in range(N):
    if B[i] == A[0]:
        pos = i
        break
    
# check if B is reversed
reverse = False
if B[(pos+1)%N] == A[-1]:
    reverse = True

# traverse and check if same
valid = True
for i in range(N):
    if reverse:
        if A[i] != B[(pos-i)%N]:
            valid = False
    else:
        if A[i] != B[(pos+i)%N]:
            valid = False

if valid:
    print('good puzzle')
else:
    print('bad puzzle')