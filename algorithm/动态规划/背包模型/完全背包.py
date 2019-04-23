# 每件物品无限个
def complete_pack(weight, value, c):
    n = len(weight)
    max_value = [0 for i in range(c+1)]
    for i in range(n):
        for w in range(1, c+1):
            if weight[i] > w:
                continue
            max_value[w] = max(max_value[w], max_value[w-weight[i]]+value[i])
    return max_value

if __name__ == '__main__':
    w = [2, 3, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    c = 10
    print(complete_pack(w, v, c))