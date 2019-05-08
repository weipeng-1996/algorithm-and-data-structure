def threeSum(nums):
    nums.sort()
    arr = []
    for i in range(len(nums)):
        # 判断条件 为了优化 没有也可以
        if i == 0 or nums[i] > nums[i-1]:
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if -nums[i] == nums[l] + nums[r]:
                    arr.append([nums[i], nums[l], nums[r]])
                    # l 和 r 要同时变化缩小范围，否则肯定和上一个答案一样
                    l += 1
                    r -= 1
                    # 如果变化后 l/r元素和之前相同继续缩小
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                elif -nums[i] < nums[l] + nums[r]:
                    r -= 1
                else:
                    l += 1
    return arr
