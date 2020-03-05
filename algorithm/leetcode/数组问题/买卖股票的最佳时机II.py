# 122

# O(n)


def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    profit_sum = 0
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            min_price = prices[i]
            if max_profit > 0:
                profit_sum += max_profit
                max_profit = 0
        else:
            temp = prices[i] - min_price
            if temp > max_profit:
                max_profit = temp
    if max_profit > 0:
        profit_sum += max_profit
    return profit_sum


# 简化
def maxProfit1(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit

prices = [6, 1, 3, 2, 4, 7]
print(maxProfit1(prices))
