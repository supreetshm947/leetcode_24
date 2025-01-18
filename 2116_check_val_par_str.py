def canBeValid(s: str, locked: str) -> bool:
    n = len(s)
    if n%2==1:
        return False
    open = []
    unlocked = []
    for i in range(n):
        if locked[i]=='0':
            unlocked.append(i)
        elif s[i]=="(":
            open.append(i)
        elif s[i]==")":
            if open:
                open.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False
    while open and unlocked and open[-1]<unlocked[-1]:
        open.pop()
        unlocked.pop()
    return not open
s = "(()))()))(()((()()(((()))()()()()()())))()()(()())()(()((()()((()((((((()(()()(()()())(((((())((()))))()(((((((()()())()))())((((((()(())())()((())()()((())((((())(((())(())()()))(((()()())())))((()))))()()()((()))())(())(((()()((())(())(())())()((()))())(())()(()())((((()(((())((()()())(((()(((((()))()))))))(()((())())(())))))(())(((())()()(()))())())))(((())))()()))()())))))())()(()()))(())(()())))())()))((((())(()))()(((())())(()(()))()))((()(())()()))))())(()(((((()"
locked = "110001111001011100000100011110101000100110010010011001110010111111100111000100000000101111101001111111011101001110011001001100100001100000000010100010101101100000100001000110111000111110110010111011010010100011111101110011100010010001111001010001001000111101101111111011001000100111100110101000100011011001001100110011111111111100101000100111111100000100101101000101111101000011110001001011111010011010000100100000000011101011001110000110011000100001110101100101111111110100"
print(canBeValid(s, locked))