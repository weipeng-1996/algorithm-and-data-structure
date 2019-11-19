import itertools


#def permute(nums):
#    return list(itertools.permutations(nums))


def permute(nums):
    res = []
    def backtrack(nums, temp):
        if not nums:
            res.append(temp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:], temp + [nums[i]])
    backtrack(nums, [])
    return res



            


if __name__ == '__main__':
    nums_ins = [1,2,3]
    print(permute(nums_ins))
