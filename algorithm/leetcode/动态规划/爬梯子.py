# 70

# 暴力递归O(2^n)


def climbStairs(n):
    def climb(x, n):
        if x == n:
            return 1
        if x > n:
            return 0
        return climb(x + 1, n) + climb(x + 2, n)
    return climb(0, n)

# 记忆化递归 O(n)


def climbStairs1(n):
    def climb(x, n, memo):
        if x == n:
            return 1
        if x > n:
            return 0
        if memo[x] > 0:
            return memo[x]
        memo[x] = climb(x + 1, n, memo) + climb(x + 2, n, memo)
        return memo[x]
    memo = [0] * n
    return climb(0, n, memo)


# 动态规划 O(n)

def climbStairs2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    res = [0 for _ in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[n-1]

print(climbStairs2(3))
