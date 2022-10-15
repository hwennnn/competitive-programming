# 2416. Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.hasEnd = False
        self.total = 0
​
class Trie:
    def __init__(self):
        self.root = TrieNode()
​
    def insert(self, word: str) -> None:
        curr = self.root
        
        for x in word:
            curr = curr.children[x]
            curr.total += 1
        
        curr.hasEnd = True
​
    def search(self, word: str) -> bool:
        curr = self.root
        
        for x in word:
            if x not in curr.children:
                return False
            
            curr = curr.children[x]
        
        return curr.hasEnd
​
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for x in prefix:
            if x not in curr.children:
                return False
            
            curr = curr.children[x]
        
        return True
    
    def query(self, word: str) -> int:
        curr = self.root
        total = 0
        
        for x in word:
            if x not in curr.children: break
            
            curr = curr.children[x]
            total += curr.total
        
        return total
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        N = len(words)
        res = [0] * N
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        for index, word in enumerate(words):
            res[index] = trie.query(word)
        
        return res
