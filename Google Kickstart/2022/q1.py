class Solution():
    def solve(self):
        A = input()
        B = input()
        
        n1, n2 = len(A), len(B)
        res = len(B) - len(A)
        b = iter(B)
        
        return res if all(a in b for a in A) else "IMPOSSIBLE"

if __name__ == "__main__":
    solution = Solution()
    N = int(input())
    for i in range(1, N + 1):
        print(f"Case #{i}: {solution.solve()}")
