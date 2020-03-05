# 78

# 迭代
def subsets(nums):
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res


# 递归回溯算法
def subsets1(nums):
    res = []
    n = len(nums)
    def helper(i, temp):
        res.append(temp)
        for j in range(i, n):
            helper(j+1, temp + [nums[j]])
    helper(0, [])
    return res


print(subsets1([1, 2, 3]))
