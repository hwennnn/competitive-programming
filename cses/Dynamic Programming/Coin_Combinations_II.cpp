#include <iostream>
#include <array>
#include <algorithm>
#include <vector>
#define ll long long
#define ar array

using namespace std;
const ll mod = 1e9 + 7;
const int mxN = 5e3;
int n, target;
ar<int, 2> arr[mxN];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> target;

    vector<int> coins(n);

    for (int i = 0; i < n; i++)
        cin >> coins[i];

    vector<int> dp(target + 1);
    dp[0] = 1;

    for (auto &coin : coins)
    {
        for (int i = 0; i <= target; i++)
            if (i - coin >= 0)
                (dp[i] += dp[i - coin]) %= mod;
    }

    cout << dp[target] << endl;

    return 0;
}