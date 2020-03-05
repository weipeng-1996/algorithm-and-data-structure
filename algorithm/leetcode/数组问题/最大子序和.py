# 53

# O(n2)初步暴力算法，垃圾，自己写的
def maxSubArray(nums):
    n = len(nums)
    max = -9999
    for i in range(n):
        temp = nums[i]
        if temp > max:
            max = temp
        for j in range(i+1, n):
            temp += nums[j]
            if temp > max:
                max = temp
    return max

# 优雅些的贪心

def maxSubArray1(nums):
    n = len(nums)
    current_sum = max_sum = nums[0]
    for i in range(1, n):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# 优雅的动态规划


def maxSubArray2(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        max_sum = max(max_sum, nums[i])
    return max_sum

# 高级的分治法


arr = [1, 5, -6, 10, 8]
print(maxSubArray2(arr))
