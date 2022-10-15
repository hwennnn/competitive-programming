#include <bits/stdc++.h>
using namespace std;

#define ll long long
const ll mod = 1e9 + 7;

int main()
{
    int n, total;
    cin >> n >> total;

    vector<vector<int>> dp(n + 1, vector<int>(total + 1));
    vector<vector<int>> books(n, vector<int>(2));

    for (int i = 0; i < n; i++)
        cin >> books[i][0];

    for (int i = 0; i < n; i++)
        cin >> books[i][1];

    for (int i = 1; i <= n; i++)
        for (int j = 0; j <= total; j++)
        {
            dp[i][j] = dp[i - 1][j];
            int left = j - books[i - 1][0];
            if (left >= 0)
                dp[i][j] = max(dp[i][j], dp[i - 1][left] + books[i - 1][1]);
        }

    cout << dp[n][total] << endl;
}