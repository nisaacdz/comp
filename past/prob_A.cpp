#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void solve()
{
    string s;
    cin >> s;
    int b = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
        if (s[i] != ')') {
            break;
        } else {
            b += 1;
        }
    }

    if (b > s.length() - b) {
        cout << "Yes" << ENDL;
    } else {
        cout << "No" << ENDL;
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