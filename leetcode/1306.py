# 1306. Jump Game III
# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        deq = collections.deque([(start, arr[start])])
        seen = set()
        
        while deq:
            idx, val = deq.popleft()
            
            if val == 0:
                return True
            
            left,right = idx-val, idx+val
            
            if left >= 0 and left not in seen:
                seen.add(left)
                deq.append((left, arr[left]))
            
            if right < len(arr) and right not in seen:
                seen.add(right)
                deq.append((right, arr[right]))
                    
        
        return False
        