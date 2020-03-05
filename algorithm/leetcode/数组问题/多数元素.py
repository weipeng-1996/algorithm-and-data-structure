# 169


# 哈希表 O(n) O(n)
def majorityElement(nums):
    record = {}
    for num in nums:
        record[num] = 0
    for num in nums:
        record[num] += 1
    m = max(record.values())
    for k, v in record.items():
        if v == m:
            return k

# 排序 O(nlogn) O(1)


def majorityElement1(nums):
    nums.sort()
    return nums[len(nums)//2]

# 投票 O(n) O(1)


def majorityElement2(nums):
    count = 0
    candidate = None # 投票候选人
    for num in nums:
        if count == 0:
            candidate = num
        count  += 1 if num == candidate else -1
    return candidate

record = {1: 5, 6: 9}
print(record.values())

