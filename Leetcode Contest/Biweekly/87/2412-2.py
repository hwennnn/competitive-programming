# 2412. Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions

class Solution:
    def minimumMoney(self, A: List[List[int]]) -> int:
        diff = sum(max(0, cost - cashback) for cost, cashback in A)
        res = 0
        
        for cost, cashback in A:
            res = max(res, diff - max(0, cost - cashback) + cost)
        
        return res
​
