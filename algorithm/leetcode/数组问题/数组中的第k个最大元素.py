# 215
# 排序算法联系写个快排

def quicksort(arr, left, right):
    if left >= right:
        return
    key = arr[left]
    l, r = left, right
    while l < r:
        while arr[r] >= key and l < r:
            r -= 1
        while arr[l] < key and l < r:
            l += 1
        
        arr[l], arr[r] = arr[r], arr[l]
    quicksort(arr, left, l)
    quicksort(arr, r + 1, right)

def quick(arr):
    quicksort(arr, 0, len(arr) - 1)


def findKthLargest(nums, k):
    quick(nums)
    return nums[-k]

t = [3, 2, 1, 5, 6, 4]
t.sort()
print(t)
