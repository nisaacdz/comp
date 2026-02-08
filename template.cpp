#include <bits/stdc++.h>

typedef long long ll;
typedef long double ld;
using namespace std;

const char ENDL = '\n';
const ll MOD = 1e9 + 7;

// template <typename T>
// std::ostream& operator<<(std::ostream& os, const std::vector<T>& v) {
//     os << "[";
//     for (size_t i = 0; i < v.size(); ++i) {
//         os << v[i];
//         if (i < v.size() - 1) os << ", ";
//     }
//     os << "]";
//     return os;
// }

// template <typename K, typename V>
// ostream& operator<<(ostream& os, const map<K, V>& v) {
//     os << '[';
//     auto i = 0;
//     for (auto& [pfactor, count]: v) {
//         os << '{' << pfactor << ", " << count << '}';
//         if (i++ < v.size() - 1) os << ", ";
//     }
//     os << ']';

//     return os;
// }

// struct custom_hash {
//     static uint64_t splitmix64(uint64_t x) {
//         // http://xorshift.di.unimi.it/splitmix64.c
//         x += 0x9e3779b97f4a7c15;
//         x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
//         x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
//         return x ^ (x >> 31);
//     }
//     size_t operator()(uint64_t x) const {
//         static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
//         return splitmix64(x + FIXED_RANDOM);
//     }
// };

// ll facts[200001] = {1, 1};

// int factorial(ll num) {
//     if (facts[num]) return facts[num];
//     ll res = num * factorial(num - 1) % MOD;
//     facts[num] = res;
//     return res;
// }

void solve()
{
    ll n;
    cin >> n;
    
    vector<ll> nums(n);
    
    for (auto& num: nums) {
        cin >> num;
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