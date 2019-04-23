# 冒泡
def maopao(array):
    l = len(array)
    for i in range(l):
        for j in range(1, l-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

#选择
def select_sort(array):
    l = len(array)
    for i in range(l):
        for j in range(i+1, l):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array

#插入

def insert_sort(array):
    l = len(array)
    for i in range(1, l):
        if array[i] < array[i-1]:
            temp = array[i]
            index = i
            for j in range(i-1, -1, -1):
                if array[j] > temp:
                    array[j+1] = array[j]
                    index = j
                else:
                    break
            array[index] = temp
    return array

#快排


def quick_sort(ary):
    qsort(ary, 0, len(ary)-1)


def qsort(ary, left, right):
    #快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right:
        return 
    key = ary[left]  # 取最左边的为基准数
    lp = left  # 左指针
    rp = right  # 右指针
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] < key and lp < rp:
            lp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    qsort(ary, left, lp-1)
    qsort(ary, rp+1, right)
    return ary

# 计数排序 n个数 大小为0-k之间 a为输入数组，b为输出数组,c为临时数组
def count_sort(a,k):
    c = [0 for i in range(k+1)]
    n = len(a)
    b = ['mm' for i in range(n)]
    for i in range(n):
        c[a[i]] += 1
    for j in range(1, k+1):
        c[j] += c[j-1]
    for p in range(n):
        b[c[a[p]]-1] = a[p]
        c[a[p]] -= 1
    return b



d = [2, 5, 3, 0, 2, 3, 0, 3]

#print(maopao(a))
#print(select_sort(b))
#print(insert_sort(a))
#quick_sort(b)
#print(b)
print(count_sort(d, 5))
