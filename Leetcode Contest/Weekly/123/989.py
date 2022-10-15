# 989. Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        N = len(str(k))
        if N > len(num):
            num = [0] * (N - n) + num
        n = len(num)    
        i = n - 1
        
        while k > 0:
            num[i] += k % 10
            k //= 10
            i -= 1
        
        i = n - 1
        while i >= 0:
            if num[i] > 9:
                if i - 1 >= 0:
                    num[i - 1] += num[i] // 10
                    num[i] %= 10
                else:
                    num = [num[i] // 10] + num
                    num[i + 1] %= 10
                    return num
            i -= 1
        
        return num
        
