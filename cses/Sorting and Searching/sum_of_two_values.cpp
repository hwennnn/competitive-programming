#include <bits/stdc++.h>
#define lli long long int
#define li long int
#define ld long double
using namespace std;
const lli mod = 1e9 + 7;
 
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, x, z;
	vector<pair<int, int>> arr;
	cin >> n;
    cin >> x;

    int i = 0, j = n-1;

    for (int i = 0; i < n; i++){
        cin >> z;
		arr.push_back(make_pair(z,i+1));
    }

	sort(arr.begin(), arr.end());

    while (i < j){
        if ((arr[i].first + arr[j].first) == x){
            cout << arr[i].second << " " << arr[j].second << endl;
            return 0;
        }

        else if ((arr[i].first + arr[j].first) > x){
            j--;
        }

        else{
            i++;
        }
    }

    cout << "IMPOSSIBLE" << endl;

	return 0;
}