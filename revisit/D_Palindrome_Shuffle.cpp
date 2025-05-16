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

    vector<int> freqs(26, 0);

    for (char c: s) {
        freqs[c - 'a']++;
    }

    int left = 0, right = s.length() - 1;

    while (left < right) {
        if (s[left] == s[right]) {
            freqs[s[left] - 'a'] -= 2;
            left += 1;
            right -= 1;
        } else {
            break;
        }
    }

    // ktffetfekktttteeekffkekkttfttfeftefftk

    vector<int> freqs_new_1(26, 0);

    int k = left;

    int mid = (left + right) / 2;

    for (; k <= right; k++) {
        int pos = s[k] - 'a';
        freqs_new_1[pos]++;
        if (k <= mid && freqs_new_1[pos] > freqs[pos] / 2) {
            break;
        } else if (k > mid && s[k] != s[2 * mid - k + 1]) {
            break;
        }
    }

    int shuffle = right + 1 - k;

    k = right;

    vector<int> freqs_new_2(26, 0);

    // mid + 1 + mid - k

    for (; k >= left; k--) {
        int pos = s[k] - 'a';
        freqs_new_2[pos]++;
        if (k > mid && freqs_new_2[pos] > freqs[pos] / 2) {
            break;
        } else if (k <= mid && s[k] != s[2 * mid - k + 1]) {
            break;
        }
    }

    shuffle = min(shuffle, k - left + 1);

    cout << shuffle << ENDL;
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