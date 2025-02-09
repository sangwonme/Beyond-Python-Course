N, M = map(int, input().split())
cows = list(map(int, input().split()))
candies = list(map(int, input().split()))

# candies -> [6, 1, 3] => [[0, 6], [0, 1], [0, 3]]
for i in range(len(candies)):
    candies[i] = [0, candies[i]]

# simulation
for i in range(len(candies)):
    for j in range(len(cows)):
        # break if no candy
        if candies[i][1] == candies[i][0]:
            break
        # eat if cow's height >= base of candy
        if cows[j] >= candies[i][0]:
            # height
            height = min(cows[j], candies[i][1]) - candies[i][0]
            # eat
            candies[i][0] = min(cows[j], candies[i][1])
            # grow
            cows[j] += height

for i in range(len(cows)):
    print(cows[i])