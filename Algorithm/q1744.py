# input
n = int(input())
pos, neg, zero, ones = [], [], False, 0
for i in range(n):
  tmp = int(input())
  if tmp > 1:
    pos.append(tmp)
  elif tmp < 0:
    neg.append(tmp)
  elif tmp == 1:
    ones += 1
  else:
    zero = True

# sort
pos.sort(reverse = True)
neg.sort()

# pop neg w/ smallest abs if there is zero
if zero and len(neg) % 2 == 1:
  neg.pop(-1)

# get sum
result = ones
for i in range(len(pos)):
  if i == len(pos) - 1 and i % 2 == 0:
    result += pos[i]
  elif i % 2 == 0:
    result += pos[i] * pos[i + 1]
for i in range(len(neg)):
  if i == len(neg) - 1 and i % 2 == 0:
    result += neg[i]
  elif i % 2 == 0:
    result += neg[i] * neg[i + 1]

print(result)