#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void solve()
{
    ll h, d;
    cin >> h >> d;

    ll lo = 0, hi = d;

    auto can_reach = [&h, &d](ll x)
    {
        ll vc = (d + x) / (x + 1);
        ll vf = d / (x + 1);

        ll countc = d % (x + 1);
        ll countf = x + 1 - countc;
        
        ll health = h + x - countc * (vc * (vc + 1) / 2) - countf * (vf * (vf + 1) / 2);

        return health > 0;
    };

    while (lo < hi)
    {
        ll mid = (lo + hi) / 2;

        if (can_reach(mid))
        {
            hi = mid;
        }
        else
        {
            lo = mid + 1;
        }
    }

    ll y = lo;

    cout << y + d << ENDL;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    std::cin >> t;
    while (t--)
        solve();
    return 0;
}
