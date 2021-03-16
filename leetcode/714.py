# 714. Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        
        if n < 2: return 0
        
        mini = prices[0] 
        
        ans = 0
        
        for i in range(1,n):
            
            if prices[i] < mini:
                mini = prices[i]
                
            elif prices[i] > mini + fee:
                ans += prices[i] - mini - fee
                mini = prices[i] - fee
                
        return ans
