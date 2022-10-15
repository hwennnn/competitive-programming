# 2075. Decode the Slanted Ciphertext
# https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution:
    def decodeCiphertext(self, s: str, rows: int) -> str:
        if rows == 1: return s
        n = len(s)
        cols = n // rows
        mat = []
        curr = []
        
        for i, x in enumerate(s):
            curr.append(x)
            
            if i == n - 1 or (i + 1) % cols == 0:
                mat.append(curr)
                curr = []
​
        res = ""
        for j in range(cols):
            i = 0
            word = mat[i][j]
            i += 1
            j += 1
            
            while i < rows and j < cols:
                word += mat[i][j]
                i += 1
                j += 1
                
            res += word
        
        return res.rstrip()
            
