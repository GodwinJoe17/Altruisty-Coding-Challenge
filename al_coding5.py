def getMaxToys(prices, money):
    start = 0
    current_sum = 0
    maxtoys = 0
    for end in range(len(prices)):
        current_sum += prices[end]
        while current_sum > money:
            current_sum -= prices[start]
            start += 1
        maxtoys = max(maxtoys, end - start + 1)
    return maxtoys
n = int(input("Enter the number of toys: "))
prices = list(map(int, input(f"Enter the prices of the {n} toys separated by spaces: ").split()))
money = int(input("Enter the amount of money available: "))
result = getMaxToys(prices, money)
print(result)
