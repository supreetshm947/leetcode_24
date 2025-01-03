def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i, j, k = m-1, n-1, m + n - 1
    while i > -1 and j > -1:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # while i > -1:
    #     nums1[k] = nums1[i]
    #     i -= 1
    #     k -= 1

    while j > -1:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

print(merge(nums1, 3, nums2, 3))