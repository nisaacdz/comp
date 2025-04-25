#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

ll powMod(ll num, ll pow)
{
    if (pow == 0)
        return 1;
    return (pow & 1) ? num * powMod(num, pow - 1) % MOD : powMod((num * num) % MOD, pow / 2);
}

void solve()
{
    ll n, num;
    cin >> n;
    vector<ll> nums(n);
    ll sum = 0;
    for (ll &num : nums)
    {
        cin >> num;
        sum = (sum + num) % MOD;
    }

    ll p = 0, q = (n * (n - 1)) % MOD;
    for (int i = 0; i < n - 1; i++)
    {
        sum = ((sum - nums[i]) % MOD + MOD) % MOD;
        p = (p + ((sum * nums[i]) % MOD)) % MOD;
    }
    q = (q * powMod(2, MOD - 2)) % MOD;
    ll ans = (p * powMod(q, MOD - 2)) % MOD;
    cout << ans << ENDL;
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