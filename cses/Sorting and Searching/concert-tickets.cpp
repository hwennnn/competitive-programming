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
    lli n, m, curr, ticket;
    cin >> n >> m;
    multiset<lli, greater<int>> tickets;
 
    while (n--)
    {
        cin >> ticket;
        tickets.insert(ticket);
    }
    
// 5 3
// 8 7 5 5 3
// 4 8 3

// 1 2
// 1
// 10 10
    while (m--)
    {
        cin >> curr;
        auto it = tickets.lower_bound(curr);
 
        if (it == tickets.end())
        {
            cout << -1 << endl;
        }
        else
        {
            cout << *it << endl;
            tickets.erase(it);
        }
    }
    return 0;
}