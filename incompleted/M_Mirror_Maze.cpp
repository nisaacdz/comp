#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void solve()
{
    int r, c;

    cin >> r >> c;
    vector<string> grid(r, string(""));
    

    for (auto& s: grid) {
        cin >> s;
    }


}

int traverse(int i, int j, vector<vector<int[]>>& memo, vector<vector<bool>> visited) {
    if (i < 0 || j < 0 || i >= memo.size() || j >= memo[0].size() || visited[i][j]) return 0;

    visited[i][j] = true;

    
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    solve();
    return 0;
}