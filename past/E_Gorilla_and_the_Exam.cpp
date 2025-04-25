#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

void solve()
{
    int n, k;
    cin >> n >> k;
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        mp[x]++;
    }
    
    vector<int> nums;

    for (auto& [k, v]: mp) {
        nums.push_back(v);
    }

    sort(nums.begin(), nums.end());
    
    int i = 0;

    while (i < nums.size() - 1 && k >= nums[i]) {
        k -= nums[i++];
    }

    cout << nums.size() - i << ENDL;
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