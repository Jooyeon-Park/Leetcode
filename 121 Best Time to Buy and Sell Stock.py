class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0
        i = 0
        j = 1
        maxPro = 0
        while j < len(prices):
            currentProfit = prices[j] - prices[i]
            if prices[j] - prices[i] > 0:
                maxPro = max(currentProfit, maxPro)
            else:
                i = j
            j += 1
        return maxPro

