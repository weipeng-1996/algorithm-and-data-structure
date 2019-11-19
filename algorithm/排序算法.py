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
    qsort(ary, left, lp)
    qsort(ary, rp+1, right)

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

# 归并排序
# 合并两列表
def merge(a, b):
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    if i == len(a):
        merged.extend(b[j:])
    else:
        merged.extend(a[i:])
    return merged

# 递归分治
def merge_sort(c):
    if len(c) <= 1:
        return c
    mid = len(c) // 2
    a = merge_sort(c[:mid])
    b = merge_sort(c[mid:])
    return merge(a, b)



#d = [7,5,9,10,8,3,1]
#print(maopao(a))
#print(select_sort(b))
#print(insert_sort(a))
#quick_sort(b)
#print(b)
#a = quick_sort(d)
#print(d)
c = [7, 9, 1, 0, 4, 3, 8, 2, 5, 4, 6]
print(merge_sort(c))
print(c)
