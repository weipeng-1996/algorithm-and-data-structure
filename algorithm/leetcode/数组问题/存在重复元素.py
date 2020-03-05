# 217

# 哈希表 O(n)
def containsDuplicate(nums):
    re = {}
    for num in nums:
        try:
            re.pop(num)
            return True
        except:
            re[num] = 1
    return False
