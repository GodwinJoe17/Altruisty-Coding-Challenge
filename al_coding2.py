def wordbreak(n, s, dic):
    word_set = set(dic)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return 1 if dp[len(s)] else 0 
n = int(input("Enter the number of words in the dictionary: "))
s = input("Enter the string to check: ")
dic = input(f"Enter {n} words for the dictionary, separated by spaces: ").split()
result = wordbreak(n, s, dic)
print(result)
