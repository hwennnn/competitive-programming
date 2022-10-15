# 989. Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        carry = 0
        
        for x in num[::-1]:
            carry += x + k % 10
            res.append(carry % 10)
            carry //= 10
            k //= 10
        
        while carry > 0 or k > 0:
            carry += k % 10
            res.append(carry % 10)
            carry //= 10
            k //= 10
        
        return res[::-1]
