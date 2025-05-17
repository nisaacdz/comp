#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void solve()
{
    int n, m;
    cin >> n >> m;
    vector<string> target(n);
    for (int i = 0; i < n; i++) {
        cin >> target[i];
    }

    vector<vector<string>> nn(m, vector<string>(n));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> nn[i][j];
        }
    }

    vector<bool> needed(n, true);
    int max_v = 0;

    for (auto& net: nn) {
        int cur = 0;

        for (int i = 0; i < n; i++) {
            bool cn = target[i] == net[i];
            cur += cn;
            needed[i] = needed[i] && !cn;
        }

        max_v = max(max_v, cur);
    }
    
    if (accumulate(needed.begin(), needed.end(), 0) > 0) {
        cout << -1 << ENDL;
    } else {
        cout << n + 2 * (n - max_v) << ENDL;
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