# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]):

        def construct(words):
            mp = collections.defaultdict(set)
            
            for w in words:
                for i in range(len(w)):
                    t = w[:i] + "_" + w[i+1:]
                    mp[t].add(w)
            
            return mp
        
        def bfs(s):
            deq = collections.deque([(begin, 1)])
            visited = set()
            
            while deq:
                word, count = deq.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end: return count
                
                    for i in range(len(word)):
                        t = word[:i] + "_" + word[i+1:]

                        for nei in s[t]:
                            if nei not in visited:
                                deq.append((nei, count+1))

            return 0
        
        s = construct(set(wordList))
        return bfs(s)

    def ladderLength(self, begin: str, end: str, wordList: List[str]):
        s = set(wordList)
        deq = collections.deque([(begin, 1)])
        visited = set()
        
        while deq:
            word, count = deq.popleft()
            if word == end: return count
            
            for i in range(len(word)):
                for x in string.ascii_lowercase:
                    w = word[:i] + x + word[i+1:] 

                    if w in s and w not in visited:
                        visited.add(w)
                        deq.append((w, count+1))
        
        return 0
    
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