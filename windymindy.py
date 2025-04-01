def BuyHouse(n, heights):
    max_left = float("-inf")
    left_to_right = set()

    max_right = float("-inf")
    right_to_left = set()

    for i in range(n):
        if max_left >= heights[i]:
            left_to_right.add(i)
        else:
            max_left = heights[i]

    for i in range(n-1, -1, -1):
        if max_right >= heights[i]:
            right_to_left.add(i)
        else:
            max_right = heights[i]

    return f"{len(left_to_right)} {len(right_to_left)} {len(left_to_right.intersection(right_to_left))}"

n=17
h=[179, 282, 32, 204, 468, 306, 142, 173, 389, 422, 341, 86, 93, 377, 110, 497, 403]
print(BuyHouse(n,h))