

def threeSumClosest(nums, target):
    nums.sort()
    temp = 999999
    for i in range(len(nums)):
        l = i+1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                return target
            elif s > target:
                r -= 1
                temp = s if abs(target-s) < abs(target-temp) else temp
            else:
                l += 1
                temp = s if abs(target-s) < abs(target-temp) else temp
    return temp

if __name__ == '__main__':
    nums = [-1, 2, 1,-4]
    target = 1
    print(threeSumClosest(nums, target))
