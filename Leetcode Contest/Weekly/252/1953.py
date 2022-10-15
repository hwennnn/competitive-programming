# 1953. Maximum Number of Weeks for Which You Can Work
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        ssum, mmax = sum(milestones), max(milestones)
        
        if ssum - mmax >= mmax: return ssum
        
        return 2 * (ssum - mmax) + 1
