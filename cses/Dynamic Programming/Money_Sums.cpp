#include <bits/stdc++.h>
using namespace std;

#define ll long long
const ll mod = 1e9 + 7;

int main()
{
    int n;
    cin >> n;
    int maxSize = n * 1000;
    vector<vector<bool>> dp(n + 1, vector<bool>(maxSize + 1, false));
    dp[0][0] = true;

    vector<int> coins(n);
    for (int &coin : coins)
        cin >> coin;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= maxSize; j++)
        {
            dp[i][j] = dp[i - 1][j];
            int left = j - coins[i - 1];
            if (left >= 0 && dp[i - 1][left])
            {
                dp[i][j] = true;
            }
        }
    }

    vector<int> res;
    for (int j = 1; j <= maxSize; j++)
    {
        if (dp[n][j])
            res.push_back(j);
    }

    cout << res.size() << endl;
    for (auto x : res)
        cout << x << " ";
}