# 有N种物品和一个容量为V的背包。第i种物品最多有n[i]件可用

# 转化为01背包问题

def mul_pack(weight, value, c, num):
    max_value = [0 for i in range(c+1)]
    n = len(weight)
    for i in range(n):
        for k in range(num[i]): #把第i类物品展开
            for w in range(c, 0, -1):
                if w < weight[i]:
                    break
                max_value[w] = max(max_value[w], 
                max_value[w-weight[i]]+value[i])
    return max_value

# 二进制思想优化

def one_zero_pack(weight, value, c, max_val):
    for w in range(c, weight-1, -1):
        max_val[w] = max(max_val[w], max_val[w-weight]+value)


def complete_pack(weight, value, c, max_val):
    for w in range(weight, c+1):
        max_val[w] = max(max_val[w], max_val[w-weight]+value)


def opt_mul_pack(weight, value, c, num):
    n = len(weight)
    max_val = [0 for i in range(c+1)]
    for i in range(n):
        if (num[i]*weight[i]) > c:
            complete_pack(weight[i], value[i], c, max_val)
        else:
            k = 1
            while k < num[i]:
                one_zero_pack(weight[i]*k, value[i]*k, c, max_val)
                num[i] -= k
                k = 2*k
            one_zero_pack(weight[i]*num[i], value[i]*num[i], c, max_val)
    return max_val


if __name__ == '__main__':
    n, c = 5, 10
    weight = [2, 2, 6, 5, 4]
    value = [5, 3, 5, 4, 6]
    num = [3, 5, 2, 1, 5]
    max_value = mul_pack(weight, value, c, num)
    max_value1 = opt_mul_pack(weight, value, c, num)
    print(max_value)
    print(max_value1)
