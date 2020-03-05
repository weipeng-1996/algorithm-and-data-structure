# 62

# 时间，空间 O(m * n)
def uniquePaths(m, n):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        dp[0][i] = 1
    for j in range(n):
        dp[j][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


# 优化空间复杂度 O(2n)


def uniquePaths1(m, n):
    pre = [1] * m
    cur = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            cur[j] = pre[j] + cur[j-1]
        pre = cur[:]
    return cur[-1]

# 优化空间复杂度O(n)


def uniquePaths2(m, n):
    cur = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            cur[j] += cur[j-1]
    return cur[-1]
print(uniquePaths1(3, 2))
print([1] * 5)
