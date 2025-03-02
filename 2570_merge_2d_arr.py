from typing import List

def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    res = []
    while nums1 or nums2:
        if nums1 and nums2 and nums1[0][0]==nums2[0][0]:
            res.append([nums1[0][0], nums1.pop(0)[1]+nums2.pop(0)[1]])
        elif not nums2 or nums1 and (nums1[0][0]<nums2[0][0]):
            res.append([nums1[0][0], nums1.pop(0)[1]])
        elif not nums1 or nums2 and (nums1[0][0]>nums2[0][0]):
            res.append([nums2[0][0], nums2.pop(0)[1]])
    return res

nums1 = [[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],[757,875],[788,208],[932,695]]
nums2 = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],[177,948],[211,653],[285,775],[309,289],[349,396],[386,831],[403,318],[405,119],[420,153],[468,433],[504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[756,878],[757,952],[770,795],[806,118],[813,88],[919,501],[935,253],[982,385]]
print(mergeArrays(nums1,nums2))
