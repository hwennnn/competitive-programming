# 1619. Mean of Array After Removing Some Elements
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = int(len(arr)*0.05)
        
        arr.sort()
        count = res = 0
        
        for i in range(k,n-k):
            res += 1
            count += arr[i]
        
        return count / res
            