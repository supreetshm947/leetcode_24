from typing import List

def findDifferentBinaryString(nums: List[str]) -> str:
    n = len(nums[-1])
    def backtrack(num):
        if len(num) == n:
            if num in nums:
                return ""
            return num
        return backtrack(num+"0") or backtrack(num+"1")
    return backtrack('')
nums = ["111","011","001"]
print(findDifferentBinaryString(nums))