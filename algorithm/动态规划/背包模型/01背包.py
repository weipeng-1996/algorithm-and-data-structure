
def get_max(weight,value,n,c):
    # max_value[i][w]表示前i件物品(不是都放)放入容量为w的背包的最大价值
    max_value = [[0 for i in range(c+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, c+1):
            if weight[i-1]>w:
                max_value[i][w] = max_value[i-1][w]
            else:
                max_value[i][w] = max(max_value[i-1][w], 
                max_value[i-1][w-weight[i-1]]+value[i-1])
    return max_value

# 优化get_max,使空间复杂度由O(nc)变为O(c)
def optimize_max(weight, value, n, c):
    max_value = [0 for i in range(c+1)]
    for i in range(n):
        for w in range(c, 0, -1):
            if weight[i] > w:
                break
            max_value[w] = max(max_value[w], max_value[w-weight[i]]+value[i])
    return max_value

if __name__ == '__main__':
    n, c = 5, 10
    weight = [2, 2, 6, 5, 4]
    value = [6, 3, 5, 4, 6]
    max_value = get_max(weight, value, n, c)
    optimize_max_value = optimize_max(weight, value, n, c)
    print(max_value)
    print(optimize_max_value)
