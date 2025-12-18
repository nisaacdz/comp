#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void solve()
{
    int n, k, p, q;
    cin >> n >> k >> p >> q;
    vector<int> nums(n);
    for (auto& v: nums) {
        cin >> v;
    }

    map<int, int> lp;
    set<int> ordered_lp;

    ll ans = 0, l = 0, r = 0;

    while (r < n) {
        if (lp.size() == k && lp.count(nums[r]) == 0) {
            //cout << "too much " << r << ENDL;
            if (lp[nums[l]] == l) {
                ordered_lp.erase(l);
                lp.erase(nums[l]);
            }
            l += 1;
        } else {
            if (lp.count(nums[r]) > 0) ordered_lp.erase(lp[nums[r]]);
            ordered_lp.insert(r);
            lp[nums[r]] = r;

            if (lp.size() == k) {
                // cout << "check: r = " << r << ENDL;
                // for (auto& v: ordered_lp) {
                //     cout << v << ",";
                // }
                // cout << ENDL << "check end" << ENDL;
                int earliest = *ordered_lp.begin();
                pair<int, int> inv1 = {l, earliest};
                pair<int, int> inv2 = {r - q + 1, r - p + 1};

                //cout << "exact at r == " << r << "; pair " << inv1.first << ";" << inv1.second << " and pair2 " << inv2.first << ";" << inv2.second << ENDL;

                ans += max(0, min(inv1.second, inv2.second) - max(inv1.first, inv2.first) + 1);
                // cout << "exact " << min(inv1.second, inv2.second) << ";" << max(inv1.first, inv2.first) << ENDL;
            }
            r += 1;
        }
    }

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