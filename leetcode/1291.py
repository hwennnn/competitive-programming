# 1291. Sequential Digits
# https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int):
        
        q = collections.deque(range(1,10))
        res = []
        
        while q:
            v = q.popleft()
            if low <= v <= high:
                res.append(v)
            
            last = v%10
            
            if last < 9:
                q.append(v*10 + last + 1)
        
        return res
    

    def sequentialDigits(self, low: int, high: int):
        minl = len(str(low))
        maxl = len(str(high))
        
        res = []
        
        
        for l in range(minl, maxl+1):
            if l == minl:
                first = int(str(low)[0])
                initial = "".join([str(i) for i in range(first,first+l)])

                if len(initial) != l: continue

                nxt = int(initial[-1]) + 1
                if int(initial) < low:
                    initial = initial[1:] + str(nxt)

                if len(initial) != l: continue
            
            else:
                initial = "".join([str(i) for i in range(1,l+1)])

            start = initial
            istart = int(start)
            if low <= istart <= high:
                res.append(istart)
            
            while low <= istart <= high and str(start[-1]) != 9:
                nxt = int(start[-1]) + 1
                if len(start[1:] + str(nxt)) == l:
                    start = start[1:] + str(nxt)
                else:
                    break
                istart = int(start)
                if low <= istart <= high:
                    res.append(istart)
                

        
        return res