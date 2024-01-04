class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        k = 0
        for i in range(1,len(prices)):
            if prices[k] > prices[i]: #loss
                k += 1
            
            else:# gain or 0
                maxProfit += (prices[i] - prices[k])
                k = i
                
        return maxProfit