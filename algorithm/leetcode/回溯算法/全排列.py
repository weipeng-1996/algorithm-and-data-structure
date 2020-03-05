def permute(nums):
    def backtrack(first = 0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    n = len(nums)
    output = []
    backtrack()
    print(output)

permute([1, 2, 3])

