# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]):
        s = set(wordList)
        if end not in s: return 0
        
        def diff(w, word):
            count = 0
            for a,b in zip(w, word):
                if a != b: count += 1
                
                if count > 1: return False
            
            return True
        
        res = float('inf')

        visited = set()
        deq = collections.deque([(begin,1)])

        while deq:
            word, count = deq.popleft()
            if word == end:
                res = min(res, count)
                continue
            
            for w in wordList:
                if w not in visited and diff(w, word):
                    visited.add(w)
                    deq.append((w, count+1))
                
        return res if res != float('inf') else 0