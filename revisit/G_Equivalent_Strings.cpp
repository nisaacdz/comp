#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void is_equivalent(string& s1, string& s2, int l1, int r1, int l2, int r2, vector<vector<int>>& mega_dict1, vector<vector<int>>& mega_dict2) {
    vector<int> diff1(26, 0);
    vector<int> diff2(26, 0);

    for (int i = 0; i < 26; i++) {
        diff1[i] = mega_dict1[r1][i] - (l1 > 0 ? (mega_dict1[l1 - 1][i]): 0);
        diff2[i] = mega_dict2[r2][i] - (l2 > 0 ? (mega_dict2[21 - 1][i]): 0);
    }

    
}

void solve()
{
    string s1, s2;
    cin >> s1;
    cin >> s2;
    vector<vector<int>> mega_dict1, mega_dict2;

    vector<int> cur_dict1(26, 0), cur_dict2(26, 0);

    for (int i = 0; i < s1.size(); i++) {
        cur_dict1[s1[i] - 'a'] += 1;
        cur_dict2[s2[i] - 'a'] += 1;

        mega_dict1.push_back(cur_dict1);
        mega_dict2.push_back(cur_dict2);
    }
        
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    solve();
    return 0;
}