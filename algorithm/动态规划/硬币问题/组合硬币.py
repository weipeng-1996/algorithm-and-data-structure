'''假设我们有8种不同面值的硬币｛1，2，5，10，20，50，100，200｝，用这些硬币组合
够成一个给定的数值n。例如n=200，那么一种可能的组合方式为 
200 = 3 * 1 + 1＊2 + 1＊5 + 2＊20 + 1 * 50 + 1 * 100. 问总过有多少种可能的组合方式？
'''


def get_combination(coins, m):
    n = len(coins)
    # dp[i][j] 为 前i种面值的硬币组合成j元钱的最多组合方式
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(j//coins[i-1]+1):
                dp[i][j] += dp[i-1][j-k*coins[i-1]]
    return dp


if __name__ == '__main__':
    coins = [1,2,5,10,50,20,100,200]
    money = 200
    max_combination = get_combination(coins, money)
    print(max_combination[8][money])

