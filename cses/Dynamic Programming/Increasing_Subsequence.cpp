#include <bits/stdc++.h>
using namespace std;

#define ll long long
const ll mod = 1e9 + 7;

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums)
        cin >> x;

    vector<int> dp;

    for (int x : nums)
    {
        auto it = lower_bound(dp.begin(), dp.end(), x);

        if (it == dp.end())
        {
            dp.push_back(x);
        }
        else
        {
            *it = x;
        }
    }

    cout << dp.size() << endl;
}