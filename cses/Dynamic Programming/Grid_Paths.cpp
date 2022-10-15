#include <bits/stdc++.h>
using namespace std;

#define ll long long
const ll mod = 1e9 + 7;

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    vector<vector<char>> grid(n, vector<char>(n));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> grid[i][j];

    for (int i = 0; i < n; i++)
    {
        if (grid[i][0] == '*')
            break;
        dp[i][0] = 1;
    }

    for (int j = 0; j < n; j++)
    {

        if (grid[0][j] == '*')
            break;
        dp[0][j] = 1;
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 1; j < n; j++)
        {
            if (grid[i][j] == '*')
                continue;

            (dp[i][j] += dp[i - 1][j]) %= mod;
            (dp[i][j] += dp[i][j - 1] %= mod);
        }
    }

    cout << dp[n - 1][n - 1] % mod << endl;
}