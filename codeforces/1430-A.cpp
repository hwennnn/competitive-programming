// https://codeforces.com/contest/1430/problem/A

#include <bits/stdc++.h>
#define ll long long
#define ar array

using namespace std;
const ll M = 1000000007;
const int mxN = 1e3;

void solve(){
    int n;
    cin >> n;
    if (n < 3 || n == 4) cout << "-1";
    else if (n % 3 == 0) cout << n / 3 << " 0 0";
    else if ((n-5)%3 == 0) cout << (n-5)/3 << " 1 0";
    else cout << (n-7)/3 << " 0 1";
    cout << "\n";
}

int main()
{
    int t;
    cin >> t;
    while (t--) solve();

    return 0;
}
