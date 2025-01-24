class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in prices:
            if i < buy:
                buy = i
            elif i - buy > 0:
                profit += i - buy
                buy = i
        return profit