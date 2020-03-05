# 121

# 暴力解法O(n^2)

def maxProfit(prices):
    n = len(prices)
    maxProfit = 0
    for i in range(n):
        for j in range(i + 1, n):
            temp = prices[j] - prices[i]
            if temp > maxProfit:
                maxProfit = temp
    return maxProfit

# 一次遍历O(n)
def maxProfit1(prices):
    min_price = 999999999
    max_profit = 0
    for i in range(len(prices)):
        if min_price > prices[i]:
            min_price = prices[i]
        else:
            temp = prices[i] - min_price
            if temp > max_profit:
                max_profit = temp
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit1(prices))
