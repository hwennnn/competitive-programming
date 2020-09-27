#include <bits/stdc++.h>
#define ll long long
#define ar array

using namespace std;
const ll mod = 1e9 + 7;
const int mxN = 1e3;
int n, A[20];

int main()
{
    cin >> n;
    ll s = 0, ans = 0;
    for (int i = 0; i < n; i++){
        cin >> A[i], s += A[i];
    }

    for (int i = 0; i<1<<n; ++i){
        ll cs = 0;
        for (int j = 0; j<n; ++j)
            if (i >> j&1)
                cs += A[j];
        
        if (cs <= s/2)
            ans = max(ans, cs);
        
    }

    cout << s-2*ans;
   
    return 0;
}
