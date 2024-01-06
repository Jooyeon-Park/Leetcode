class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0
        if len(prices) == 1:
            return maxProfit

        while sell < len(prices):
            if prices[sell] < prices[buy]:#Loss
                buy = sell
            
            else: #Win
                maxProfit = max(maxProfit, prices[sell]-prices[buy])
            sell += 1

        return maxProfit