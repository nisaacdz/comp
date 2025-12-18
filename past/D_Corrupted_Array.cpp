#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void solve()
{
    ll n;
    cin >> n;
    vector<ll> nums(n + 2);
    for (auto& num: nums) {
        cin >> num;
    }

    ll sum = accumulate(nums.begin(), nums.end(), 0LL);
    multiset<ll> freqs(nums.begin(), nums.end());

    int stop = n + 2;
    
    for (int i = 0; i < n + 2; i++) {
        ll m1 = sum - nums[i];
        if (m1 % 2 == 0 && freqs.count(m1 / 2) >= 1 + (nums[i] == m1 / 2)) {
            stop = i;
            break;
        }
    }

    if (stop >= n + 2) {
        cout << -1 << ENDL;
    } else {
        ll x = nums[stop];
        ll m1 = (sum - x) / 2;
        freqs.erase(freqs.find(x));
        freqs.erase(freqs.find(m1));
        for (auto v: freqs) {
            cout << v << " ";
        }
        cout << ENDL;
    }
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