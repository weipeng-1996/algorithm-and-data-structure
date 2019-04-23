'''
  给定一个字符串str，如果可以在str的任意位置添加字符，请返回在添加字符最少的情况下，
让str整体都是回文字符串的结果。

原问题。首先考虑，如果可以在str的任意位置添加字符，最少需要添加几个字符就可以让str整体
都是回文字符串。这个问题可以使用动态规划解决。如果str的长度为N，生成N×N的dp矩阵，
dp[i][j]的含义是子串str[i…j]最少添加几个字符可以使str[i…j]整体都是回文串。
dp[i][j]的求法如下：

如果i == j，说明此时只有一个字符，本身就是回文串，dp[i][j] = 0。

如果str[i…j]有两个字符，如果这个字符相同dp[i][j] = 0。否则dp[i][j] = 1。

如果str[i…j]多于两个字母，如果str[i] == str[j]。则dp[i][j] = dp[i+1][j-1]。
否则，dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1。为什么呢？举例说明，
假设str = “ABC”，可以先将“BC”变成回文串“BCB”，然后在末尾加“A”，也可以先将“AB”变成回文串“ABA”，
然后在最前面加“C”。即可以先处理str[i+1…j]然后末尾加str[i]，也可以先处理str[[i…j-1]
然后开头加str[j]。
接下来介绍如何根据dp矩阵，求在添加字符最少的情况下，让str整体都是回文字符串的一种结果。首先，
dp[0][N-1]的值代表整个字符串最少需要添加几个字符，所以，如果最后的结果记为字符串res，
res的长度为 N + dp[0][N-1]，然后依次设置res左右两头的字符。具体过程如下：

如果str[i] == str[j]，那么str[i…j]变成回文串的最终结果为 
str[i] + str[i+1][j-1]变成回文串的结果 + str[j]，此时res的左右两头字符为str[i]，
然后根据str[i+1][j-1]和矩阵dp确定res的中间部分。

如果str[i] != str[j]，判断dp[i][j-1]和dp[i+1][j]哪个小，如果dp[i][j-1]小，
那么str变成回文串的结果为 str[j] + str[i][j-1]变成回文串的结果 + str[j]，此时res左右
两头的字符为str[j]，然后根据str[i][j-1]和矩阵dp确定res的中间部分。
如果dp[i+1][j]小，过程同上。
'''
# 求最小插入字符数

def min_num(str):
    l = len(str)
    dp = [[0 for i in range(l)] for j in range(l)]
    for i in range(1, l):
        dp[i-1][i] = 0 if str[i-1] == str[i] else 1
        for j in range(i-2, -1, -1):
            if str[j] == str[i]:
                dp[j][i] = dp[j+1][i-1]
            else:
                dp[j][i] = min(dp[j+1][i], dp[j][i-1]) + 1
    return dp

# 获取最少插入后的回文串
def get_str(str, dp):
    l = len(str)
    res = [0 for i in range(l+dp[0][l-1])]
    length = len(res)
    resl = 0
    resr = length - 1
    i = 0
    j = l-1
    while(i <= j):
        if str[i] == str[j]:
            res[resl] = str[i]
            res[resr] = str[j]
            i += 1
            j -= 1
        elif dp[i+1][j] < dp[i][j-1]:
            res[resl] = str[i]
            res[resr] = str[i]
            i += 1
        else:
            res[resl] = str[j]
            res[resr] = str[j]
            j -= 1
        resl += 1
        resr -= 1
    return ''.join(res)

if __name__ == '__main__':
    s = input()
    l = len(s)
    dp = min_num(s)
    print(dp)
    r = get_str(s, dp)
    print(r)
