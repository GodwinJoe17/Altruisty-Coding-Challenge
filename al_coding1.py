def uni_num(arr):
    xor_all = 0
    for num in arr:
        xor_all ^= num
    set_bit = xor_all & -xor_all
    num1, num2 = 0, 0
    for num in arr:
        if num & set_bit:
            num1 ^= num
        else:
            num2 ^= num
    return sorted([num1, num2])
i = list(map(int, input("Enter the numbers separated by spaces: ").split()))
print(uni_num(i))
