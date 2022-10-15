class Solution():
    def solve(self):
        s = list(input().strip())
        n = len(s)
        
        count = sum(int(x) for x in s)
        
        count = 9 - count % 9
        if count == 9:
            count = 0
        
        res = []
        
        if count == 0:
            res = [s[0]] + ["0"] + s[1:]
        else:
            index = 0

            while index < n and int(s[index]) <= count:
                res.append(str(s[index]))
                index += 1
            
            res.append(str(count))
            
            while index < n:
                res.append(str(s[index]))
                index += 1
        
        return "".join(res)

if __name__ == "__main__":
    solution = Solution()
    N = int(input())
    for i in range(1, N + 1):
        print(f"Case #{i}: {solution.solve()}")
