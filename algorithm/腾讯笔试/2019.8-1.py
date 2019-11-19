import sys

if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    i = 0
    l = len(arr)
    arr_count = [2 for i in range(l)]
    for j in range(1, l-1):
        arr_count[j] += 1
    while i < l:
        if l == 1:
            print(1)
            break
        right = i + 2
        if right < l:
            rmax = arr[i+1]
        while right < l:
            if arr[right] > rmax:
                arr_count[i] += 1
                rmax = arr[right]
            right += 1
        left = i - 2
        if left > -1:
            lmax = arr[i-1]
        while left > -1:
            if arr[left] > lmax:
                arr_count[i] += 1
                lmax = arr[left]
            left -= 1
        i += 1
    for i in range(n):
        if i == n-1:
            print(arr_count[i], end = '')
            break
        print(arr_count[i], end = ' ')