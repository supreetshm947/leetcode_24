def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    symbol_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    sum = 0
    cont = False
    for i, c in enumerate(s):
        if cont:
            sum += symbol_map[c] - symbol_map[s[i - 1]]
            cont = False
        elif i == len(s) - 1 or symbol_map[c] >= symbol_map[s[i + 1]]:
            sum += symbol_map[c]
        else:
            cont = True

    return sum

print(romanToInt("MCMXCIV"))