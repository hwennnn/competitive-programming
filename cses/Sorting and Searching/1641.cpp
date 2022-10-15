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
ar<int,2> arr[mxN];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> x;

    for (int i=0; i<n; ++i){
        cin >> arr[i][0], arr[i][1]=i+1;
    }
    sort(arr, arr+n);

    for (int i=0; i<n-2; i++){
        ll a = arr[i][0];
        ll l = i+1, r = n-1;

        while (l < r){
            ll s = a + arr[l][0] + arr[r][0];

            if (s == x){
                cout << arr[i][1] << " " << arr[l][1] << " " << arr[r][1] << endl;
                return 0;
            }
            else if (s > x){
                --r;
            }else{
                ++l;
            }
        }
    }

    cout << "IMPOSSIBLE";
    return 0;
}
