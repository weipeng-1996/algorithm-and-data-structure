# 88

# 双指针由前向后
# 时间O(m+n) 空间O(m)
def merge(nums1, m, nums2, n):
    nums3 = nums1[:m]
    nums1[:] = []
    i = j = 0
    while i < m and j < n:
        if nums3[i] <= nums2[j]:
            nums1.append(nums3[i])
            i += 1
        else:
            nums1.append(nums2[j])
            j += 1
    if i < m:
        nums1[i+j:] = nums3[i:m]
    if j < n:
        nums1[i+j:] = nums2[j:n] 


# 双指针由后向前
# 时间O(m+n) 空间O(1)

def merge1(nums1, m, nums2, n):
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1
    while p1 >= 0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    nums1[:p2+1] = nums2[:p2+1]




nums1 = [11, 12, 19, 0, 0, 0, 0, 0]
nums2 = [2, 5, 6, 8, 10]
merge1(nums1, 3, nums2, 5)
print(nums1) 
