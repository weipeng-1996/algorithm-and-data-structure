# 136
# O(n^2) 列表操作


def singleNumber(nums):
    stack = []
    for num in nums:
        if num in stack:
            stack.remove(num)
        else:
            stack.append(num)
    return stack.pop()

# O(n) 字典


def singleNumber1(nums):
    hash = {}
    for num in nums:
        try:
            hash.pop(num)
        except:
            hash[num] = 1
    return hash.popitem()[0]

# O(n) 数学


def singleNumber2(nums):
    return 2 * sum(set(nums)) - sum(nums)
    

# 异或 O(n)
def singleNumber3(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


print(singleNumber3([4, 1, 2, 1, 2]))
