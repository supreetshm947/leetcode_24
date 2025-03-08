from typing import List

def closestPrimes(left: int, right: int) -> List[int]:
    sieve = [True] * (right+1)
    sieve[0] = sieve[1] = False

    for i in range(2, right+1):
        if sieve[i]:
            for number in range(i*i, right+1, i):
                sieve[number] = False

    prime_numbers = [i for i in range(left, right+1) if sieve[i]]

    if len(prime_numbers) <2:
        return [-1, -1]

    distance = float("inf")
    pair = [-1,-1]

    for i in range(len(prime_numbers)-1):
        diff = prime_numbers[i+1] - prime_numbers[i]
        if diff < distance:
            distance = diff
            pair = [prime_numbers[i],prime_numbers[i+1]]

    return pair


left = 10
right = 19
print(closestPrimes(left, right))