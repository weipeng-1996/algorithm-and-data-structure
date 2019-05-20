# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

# 二分法
def search(nums, target):
    l = len(nums)
    if l == 0:
        return -1
    left = 0
    right = l - 1
    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        # 判断左区是否有序
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 左区无序的话右区肯定有序
        else:
            # 如果在右区
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            # target在左区
            else:
                right  = mid - 1
    return left if nums[left] == target else -1




nums = [1,3,5]
target = 1

print(search(nums, target))
