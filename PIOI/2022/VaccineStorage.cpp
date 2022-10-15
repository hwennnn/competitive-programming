#include <bits/stdc++.h>

#define ll long long
#define lli long long int
#define li long int
#define ld long double
using namespace std;
const lli mod = 1e9 + 7;

int solve()
{
    int N;
    cin >> N;

    stack<int> s;

    for (int i = 0; i < N; i++)
    {
        string x;
        cin >> x;

        if (x == "Finish")
        {
            if (s.size() == 0)
                return 0;

            return s.top();
        }
        else if (x == "Combine")
        {
            if (s.size() < 2)
                return -1;
            else
            {
                int first = s.top();
                s.pop();
                int second = s.top();
                s.pop();
                s.push(first + second);
            }
        }
        else if (x == "Inject")
        {
            if (s.size() == 0)
                return -1;
            else
                s.pop();
        }
        else
        {
            int value;
            cin >> value;

            s.push(value);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cout << solve();

    return 0;
}