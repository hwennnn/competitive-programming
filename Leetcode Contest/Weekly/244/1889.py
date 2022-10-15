# 1889. Minimum Space Wasted From Packaging
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        res = float('inf')
        packages.sort()
        ss = sum(packages)
        
        for box in boxes:
            curr = last = 0
            
            for b in sorted(box):
                index = bisect.bisect(packages, b)
                curr += b * (index - last)
                last = index
            
            if last == len(packages):
                res = min(res, curr - ss)
​
        return -1 if res == float('inf') else res % M
