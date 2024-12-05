def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    n = len(nums)

    def backtrack(arr, nums):
        if len(arr) == n:
            result.append(arr)
        for i in range(len(nums)):
            backtrack(arr+[nums[i]], nums[:i] + nums[i + 1:])
    result = []
    backtrack([], nums)
    return result
nums = [1]
print(permute(nums))
