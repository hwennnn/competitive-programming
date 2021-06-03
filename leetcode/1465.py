# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    def maxArea(self, hn: int, wn: int, h: List[int], v: List[int]) -> int:
        if len(h) == 1 and h[0] == hn:
            h = [0, hn]
        else:
            h.append(0); h.append(hn)
        if len(v) == 1 and v[0] == wn:
            v = [0, wn]
        else:
            v.append(0); v.append(wn)
            
        h.sort()
        v.sort()
        
        M = 10 ** 9 + 7
        h_diff = float('-inf')
        v_diff = float('-inf')
        
        for i in range(1, len(h)):
            h_diff = max(h_diff, h[i] - h[i - 1])
        
        for i in range(1, len(v)):
            v_diff = max(v_diff, v[i] - v[i - 1])
        
        return (h_diff * v_diff) % M
