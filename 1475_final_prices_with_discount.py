from typing import List

def finalPrices(prices: List[int]) -> List[int]:
    output = prices.copy()
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            prices[stack.pop()] -= prices[i]
        stack.append(i)
    return prices

prices = [10,1,1,6]
print(finalPrices(prices))