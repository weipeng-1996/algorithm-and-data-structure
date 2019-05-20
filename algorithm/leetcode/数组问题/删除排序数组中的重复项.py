

def removeDuplicates(nums):
    l = len(nums)
    if l == 0:
        return 0
    i = 0 
    for j in range(1, l):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
        
    



if __name__ == '__main__':
    nums = [1,1,2]
    print(removeDuplicates(nums))