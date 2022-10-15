# 1720. Decode XORed Array
# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int):
        res = [first]
        
        for i in range(len(encoded)):
            res.append(res[-1] ^ encoded[i])
        
        return res