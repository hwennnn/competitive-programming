# 1640. Check Array Formation Through Concatenation
# https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]):
        mp = {x[0]:x for x in pieces}
        
        res = []
        
        for num in arr:
            res += mp.get(num, [])
        
        return arr == res
    
    def canFormArray(self, arr: List[int], pieces: List[List[int]]):
        n = len(arr)
        visited = set()
        i = 0
        
        while i < n:
            if arr[i] in pieces:
                i += 1
                visited.add(pieces.index(arr[i]))
            else:
                found = False
                j = 0
                while j < n and not found:
                    sub = arr[i:j+1]
                    if sub in pieces and pieces.index(sub) not in visited:
                        found = True
                        visited.add(pieces.index(sub))
                        break

                    j += 1

                if not found: return False
                else: i = j + 1

    def canFormArray(self, arr: List[int], pieces: List[List[int]]):
        n1 = len(arr)
        n2 = len(pieces)
        
        tmp = []
        for i in range(n1):
            tmp.append(arr[i])

            if tmp in pieces:
                tmp = []
        
        return len(tmp) == 0

                    
        return True
