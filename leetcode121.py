# Best time to buy and sell stock


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        min_buy = prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        return profit
