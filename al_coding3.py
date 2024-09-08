from collections import deque
def stepnum(N, M):
    result = []
    if N == 0:
        result.append(0)
    queue = deque(range(1, 10))
    while queue:
        num = queue.popleft()
        if N <= num <= M:
            result.append(num)
        if num == 0 or num > M:
            continue
        last_digit = num % 10
        next_num1 = num * 10 + (last_digit - 1)
        next_num2 = num * 10 + (last_digit + 1)
        if last_digit > 0:
            queue.append(next_num1)
        if last_digit < 9:
            queue.append(next_num2)    
    return sorted(result)
N, M = map(int, input("Enter the values of N and M separated by a space: ").split())
stepnum = stepnum(N, M)
print(' '.join(map(str, stepnum)))
