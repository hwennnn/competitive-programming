#include <bits/stdc++.h>
#define ll long long
#define ar array

using namespace std;
const ll mod = 1e9 + 7;
const int mxN = 1e3;
int n, a, b;

int main()
{
    cin >> n >> a >> b;

    vector<ll> prefix(n+1);
    prefix[0] = 0;
    for(int i=1;i<=n;i++){
        int x;
        cin>>x;
        prefix[i] = prefix[i-1] + x;
    }
    multiset<ll> curr;
    ll res = -2e18;
    for (int i = a; i <= n; i++){
        if (i > b){
            curr.erase(curr.find(prefix[i-b-1]));
        }
        curr.insert(prefix[i-a]);
        res = max(res, prefix[i] - *curr.begin());
            
    }

    cout << res;
   
    return 0;
}
