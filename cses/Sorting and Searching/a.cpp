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

	int numBottles = 15, numExchange = 4;
	int res = numBottles;

	while (numBottles >= numExchange){
		int remain = numBottles%numExchange;
		numBottles /= numExchange;
		res += numBottles;
		numBottles += remain;
	}
	
	cout << res;
}