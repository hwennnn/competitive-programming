# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        nums = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        deq = collections.deque([""])   
        
        for d in map(int, digits):
            tmp = []
            
            while deq:
                curr = deq.popleft()
                for digit in nums[d]:
                    tmp.append(curr+digit)
            
            for e in tmp:
                deq.append(e)
​
        
        return list(deq)
​
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits: return []
        
        dic = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        
        self.dfs(dic, digits, 0, "", res)
        
        return res
    
    def dfs(self, dic, digits, index, curr, res):
        if len(curr) == len(digits):
            res.append(curr)
            return
​
        for c in dic[digits[index]]:
            self.dfs(dic, digits, index+1, curr+c, res)
