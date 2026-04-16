class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
                if prices[i] < minVal:
                        minVal = prices[i]
                if (prices[i] - minVal) > maxProfit:
                        maxProfit = prices[i] -minVal
                
        return maxProfit
