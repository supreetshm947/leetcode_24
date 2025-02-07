def areAlmostEqual( s1: str, s2: str) -> bool:
    first_index = 0
    last_index = 0
    num_mismatches = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            num_mismatches += 1
            if num_mismatches > 2:
                return False
            elif num_mismatches == 1:
                first_index = i
            else:
                last_index = i

    return s1[first_index] == s2[last_index] and s1[last_index] == s2[first_index]


s1 = "kelb"
s2 = "kelb"
print(areAlmostEqual(s1, s2))