class Solution():
    def solve(self):
        A, B = map(int, input().split())
        res = 0
        
        def good(x):
            product = 1
            total = 0
            
            while x > 0:
                k = x % 10
                product *= k
                total += k
                x //= 10
            
            return product % total == 0
        
        for x in range(A, B + 1):
            if good(x):
                res += 1
        
        return res
        

if __name__ == "__main__":
    solution = Solution()
    N = int(input())
    for i in range(1, N + 1):
        print(f"Case #{i}: {solution.solve()}")
