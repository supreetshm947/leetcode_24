def mySqrt(x: int) -> int:
    if x<2:
        return x
    left=2
    right=x//2
    while right>=left:
        mid=(left+right)//2
        sq = mid*mid
        if sq==x:
            return mid
        elif sq>x:
            right=mid-1
        else:
            left=mid+1
    return right

x = 6
print(mySqrt(x))