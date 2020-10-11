// https://codeforces.com/contest/1430/problem/C

#include <bits/stdc++.h>
#define ll long long
#define ar array

using namespace std;
const ll M = 1000000007;
const int mxN = 1e3;

void solve(){
    int n;
    cin >> n;
    if (n == 2){
        cout << "2" << endl;
        cout << "1 2" << endl;
        return;
    }

    cout << "2" << endl;
    cout << n-2 << " " << n << endl;
    cout << n-1 << " " << n-1 << endl;

    for (ll i = n-3; i >=1; i--){
        cout << i << " " << i+2 << endl;
    }



}

int main()
{
    int t;
    cin >> t;
    while (t--) solve();

    return 0;
}
