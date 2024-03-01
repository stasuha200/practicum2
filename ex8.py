a = list(map(int, input().split()))
friends = a[0]
candies = a[1]
print(int(candies / (friends + 1)))
