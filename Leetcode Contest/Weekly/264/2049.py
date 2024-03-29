# 2049. Count Nodes With the Highest Score
# https://leetcode.com/problems/count-nodes-with-the-highest-score

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        nodes = collections.defaultdict(list)
        freq = collections.defaultdict(int)
        
        for i, x in enumerate(parents):
            if x >= 0:
                nodes[x].append(i)
        
        def go(x):
            left = right = 0
            
            if len(nodes[x]) >= 1:
                left = go(nodes[x][0])
            
            if len(nodes[x]) > 1:
                right = go(nodes[x][1])
            
            f = (left or 1) * (right or 1) * (len(parents) - 1 - left - right or 1)
            freq[f] += 1
            
            return 1 + left + right
        
        go(0)
        return freq[max(freq)]
