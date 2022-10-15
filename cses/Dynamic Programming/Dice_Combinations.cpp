#include <iostream>
#include <array>
#include <algorithm>
#include <vector>
#define ll long long
#define ar array

using namespace std;
const ll mod = 1e9 + 7;
const int mxN = 5e3;
int n;
ll x;
ar<int, 2> arr[mxN];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> x;

    vector<int> A(n + 1);
    A[0] = 1;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= 6 && i - j >= 0; j++)
        {
            A[i] = (A[i] + A[i - j]) % mod;
        }
    }

    cout << A[n];

    return 0;
}