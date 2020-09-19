#include <iostream>
#include <array>
#include <algorithm>  
#include <vector>
#define ll long long
#define ar array

using namespace std;
const ll mod = 1e9 + 7;
const int mxN = 2e5;
int n, a[mxN], v[mxN];

int main()
{
    cin >> n;

    for (int i = 0; i < n; ++i){
        cin >> a[i];
        v[i] = i-1;
        while (a[v[i]]>=a[i])
            v[i] = v[v[i]];
        
        cout << v[i]+1 << " ";

    }

   
    return 0;
}
