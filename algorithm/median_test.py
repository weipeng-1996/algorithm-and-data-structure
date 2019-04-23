
def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    l1 = len(nums1)
    if l1 % 2 == 0:
        temp1 = l1 // 2-1
        temp2 = l1 // 2
        median = (nums1[temp1]+nums1[temp2])/2
    else:
        median = nums1[l1//2]
    return median


print(findMedianSortedArrays([1,2],[3,4]))