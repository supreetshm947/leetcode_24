def minSubArrayLen( target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    n = len(nums)
    curr_sum = 0
    subarray_len = float("inf")
    for r in range(n):
        curr_sum += nums[r]
        while curr_sum >= target:
            subarray_len = min(subarray_len, r - l + 1)
            curr_sum -= nums[l]
            l += 1

    return 0 if subarray_len is float("inf") else subarray_len

nums = [2,3,1,2,4,3]
target = 7
print(minSubArrayLen(target, nums))