def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    k = k % n
    if k:
        nums[:] = nums[-k:]+nums[:n-k]
    return nums
nums = [1,2]
k=3

print(rotate(nums, k))
# nums = [-1,-100,3,99]
# k=2
# print(rotate(nums, k))