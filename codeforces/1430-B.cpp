// https://codeforces.com/contest/1430/problem/B

#include <bits/stdc++.h>
#define ll long long
#define ar array

using namespace std;
const ll M = 1000000007;
const int mxN = 1e3;

void solve(){
    int n, k;
    cin >> n >> k;
    ll A[n];
    for (ll i = 0; i < n; i++) cin >> A[i];
    sort(A, A+n);

    for (int i = n-2, c = 0; i >= 0 && c < k; i--, c++){
        A[n-1] += A[i];
        A[i] = 0;
    }
    
    cout << A[n-1] - 0 << endl;
}

// void solve(){
//     int n, k;
//     cin >> n >> k;
//     ll A[n];
//     for (ll i = 0; i < n; i++) cin >> A[i];
//     sort(A, A+n);
//     reverse(A, A+n);

//     ll s = 0;
//     for (ll i = 0; i < k+1; i++) s += A[i];
//     cout << s << endl;
// }

int main()
{
    int t;
    cin >> t;
    while (t--) solve();

    return 0;
}
