def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_map = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    def get_closest_lower_roman_key(num):
        return max(filter(lambda x: num >= x, roman_map.keys()))

    def get_closest_higher_roman_key(num):
        for i in roman_map.keys():
            if num <= i:
                return i

    nums = [int(i) for i in str(num)]
    n = len(nums) - 1
    out = ""
    for i in nums:
        t = i * (10 ** n)
        n -= 1
        if i in [4, 9]:
            k = get_closest_higher_roman_key(t)
            t = k - t
            print(t)
            out += roman_map[t]
            out += roman_map[k]
            continue
        while t > 0:
            k = get_closest_lower_roman_key(t)
            r = roman_map[k]
            out += r
            t -= k

    return out

print(intToRoman(3749))