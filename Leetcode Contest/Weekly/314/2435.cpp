// 2435. Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

const long long M = 1000000007;
​ class Solution
{
public:
       int go(vector<vector<int>> &grid, vector<vector<vector<long long>>> &cache, int rows, int cols, int k, int i, int j, int curr)
    {
               if (cache[i][j][curr] != -1)
        {
                       return cache[i][j][curr];
                 
        }
               
        if (i == rows - 1 && j == cols - 1)
        {
                       return (long long)curr == 0;
                 
        }
               
        long long count = 0;
               
        if (i + 1 < rows)
        {
                       count += (go(grid, cache, rows, cols, k, i + 1, j, (curr + grid[i + 1][j]) % k) + M) % M;
                 
        }
               
        if (j + 1 < cols)
        {
                       count += (go(grid, cache, rows, cols, k, i, j + 1, (curr + grid[i][j + 1]) % k) + M) % M;
                 
        }
               
        cache[i][j][curr] = count % M;
               
        return cache[i][j][curr];
         
    }
       
    int numberOfPaths(vector<vector<int>> &grid, int k)
    {
               int rows = grid.size(), cols = grid[0].size();
               vector<vector<vector<long long>>> cache(rows, vector<vector<long long>>(cols, vector<long long>(k + 1, -1)));
               
        
        return go(grid, cache, rows, cols, k, 0, 0, grid[0][0] % k);
         
    }
};
​
