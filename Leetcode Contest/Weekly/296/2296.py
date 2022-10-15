# 2296. Design a Text Editor
# https://leetcode.com/problems/design-a-text-editor/

class TextEditor:
​
    def __init__(self):
        self.A = ""
        self.cursor = 0
        self.N = 0
​
    def addText(self, text: str) -> None:
        p = self.N - self.cursor
        self.N += len(text)
        
        self.A = self.A[:p] + text + self.A[p:]
​
    def deleteText(self, k: int) -> int:
        p = self.N - self.cursor
        to_delete = min(k, p)
        
        self.A = self.A[:p - to_delete] + self.A[p:]
        
        self.N = len(self.A)
​
        return to_delete
​
    def cursorLeft(self, k: int) -> str:
        self.cursor = min(self.N, self.cursor + k)
​
        res = []
        n = min(10, self.N - self.cursor)
        
        for i in range(self.N - self.cursor - 1, -1, -1):
            res.append(self.A[i])
            
            if len(res) == n:
                break
        
        return "".join(res[::-1])
​
    def cursorRight(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        
        res = []
        n = min(10, self.N - self.cursor)
        
        for i in range(self.N - self.cursor - 1, -1, -1):
            res.append(self.A[i])
            
            if len(res) == n:
                break
        
        return "".join(res[::-1])
​
​
# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
