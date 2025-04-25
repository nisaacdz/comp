#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

/*
3
3
2 2 1
4
3 1 2 1
5
1 2 2 4 4
*/

void solve()
{
    ll n;
    cin >> n;
    vector<ll> nums(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    vector<ll> mines(n), maxes(n);
    maxes[0] = nums[0];
    mines[n - 1] = nums[n - 1];
    for (int i = 1; i < n; i++) {
        maxes[i] = max(maxes[i - 1], nums[i]);
    }
    for (int j = n - 2; j >= 0; j--) {
        mines[j] = min(mines[j + 1], nums[j]);
    }
    bool found = false;
    for (int k = 1; k < n && !found; k++) {
        if (maxes[k - 1] <= mines[k]) {
            found = true;
        }
    }

    if (found) {
        cout << "NO" << ENDL;
    } else {
        cout << "YES" << ENDL;
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