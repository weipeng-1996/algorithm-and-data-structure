# 231

# O(logn)
def isPowerOfTwo(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1


# 位运算
# 若 n = 2 ^ x  
#   且 x 为自然数（即 n 为 2 的幂），则一定满足以下条件：
# 恒有 n & (n - 1) == 0，这是因为：
# n 二进制最高位为 1，其余所有位为 0；
# n−1 二进制最高位为 0，其余所有位为 1；
# 一定满足 n > 0。

# O(1)
def isPowerOfTwo(n):
    return n > 0 and n & (n - 1) == 0
