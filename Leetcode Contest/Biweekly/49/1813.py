# 1813. Sentence Similarity III
# https://leetcode.com/problems/sentence-similarity-iii

class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1 = s1.split()
        s2 = s2.split()
        
        def good(a, b):
            a = collections.deque(a)
            b = collections.deque(b)
            
            while len(a) > 0 and len(b) > 0 and a[0] == b[0]:
                a.popleft()
                b.popleft()
            
            while len(a) > 0 and len(b) > 0 and a[-1] == b[-1]:
                a.pop()
                b.pop()
            
            return len(a) == 0
        
        return good(s1, s2) or good(s2, s1)
    
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(), sentence2.split()
        n1, n2 = len(s1), len(s2)
​
        if n1 > n2: return self.areSentencesSimilar(sentence2, sentence1)
​
        i = 0
        while i < n1 and s1[i] == s2[i]:
            i += 1
​
        while i < n1 and s1[i] == s2[n2 - n1 + i]:
            i += 1
​
        return i == n1
