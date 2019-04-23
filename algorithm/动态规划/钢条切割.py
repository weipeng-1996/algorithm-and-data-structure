# 寻找最优子结构，自底向上
# 钢条切割问题
def get_max(n):
    if n <= 1:
        return n
    arr = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    if n > 10:
        for i in range(11, n+1):
            arr.append(-1)
    for i in range(2, n+1):
        for j in range(1, i):
            arr[i] = max(arr[i], arr[i-j]+arr[j])
    return arr[n]

# 自顶向下
# arr为价格列表，n为切割长度, max_profit为记录最大收益列表
def top_to_bottom(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    max_profit = [-1 for i in range(n+1)]
    return top_to_bottom_temp(max_profit, n, arr)

def top_to_bottom_temp(max_profit, n, arr):
    if n > len(arr):
        temp = -1
    else:
        temp = arr[n-1]
    if max_profit[n] != -1:
        return max_profit[n]
    for i in range(1, n):
        if i > (n-i):
            break
        temp = max(temp, arr[i-1]+top_to_bottom_temp(max_profit, n-i, arr))
    if n >= 11:
        arr.append(temp)
    max_profit[n] = temp
    return max_profit[n]
    
    


    

if __name__ == '__main__':
    a = get_max(100)
    print(a)
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    b = top_to_bottom(price, 100)
    print(b)
