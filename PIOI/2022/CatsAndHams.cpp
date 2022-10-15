#include <bits/stdc++.h>

#define ll long long
#define lli long long int
#define li long int
#define ld long double
using namespace std;
const lli mod = 1e9 + 7;
const ll fullMask = (1 << 16) - 1;
unordered_map<string, int> A = {{"cccc", 0}, {"ccch", 1}, {"cchc", 2}, {"cchh", 3}, {"chcc", 4}, {"chch", 5}, {"chhc", 6}, {"chhh", 7}, {"hccc", 8}, {"hcch", 9}, {"hchc", 10}, {"hchh", 11}, {"hhcc", 12}, {"hhch", 13}, {"hhhc", 14}, {"hhhh", 15}};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<ll> mp(1 << 16, 0);
    mp.clear();
    vector<ll> B;
    ll res = 0;

    for (int i = 0; i < n; i++)
    {
        string x;
        cin >> x;
        ll mask = 0;
        for (int i = 0; i < x.length(); i += 4)
        {
            mask |= (1 << A[x.substr(i, 4)]);
        }

        mp[mask] += 1;
        B.push_back(mask);
    }

    for (int mask : B)
    {
        int target = fullMask ^ mask;

        res += mp[target];
    }

    cout << res / 2;
    return 0;
}