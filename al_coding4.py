def minticketprice(tickets, K):
    stack = []
    for digit in tickets:
        while stack and K > 0 and stack[-1] > digit:
            stack.pop()
            K -= 1
        stack.append(digit)
    while K > 0:
        stack.pop()
        K -= 1
    minprice = ''.join(stack).lstrip('0')
    return minprice if minprice else '0'
tickets = input("Enter the ticket price: ")
K = int(input("Enter the number of digits to remove: "))
result = minticketprice(tickets, K)
print(result)
