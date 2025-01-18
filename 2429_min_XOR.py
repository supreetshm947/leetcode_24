def minimizeXor(num1: int, num2: int) -> int:
    b_1 = bin(num1)
    b_2 = bin(num2)
    n_1 = b_1.count('1')
    n_2 = b_2.count('1')
    print(b_1, b_2, n_1, n_2)

num1 = 3
num2 = 5
print(minimizeXor(num1, num2))