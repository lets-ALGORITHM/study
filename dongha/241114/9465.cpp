#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#define ll long long
#define fastio cin.tie(0)->sync_with_stdio(0);
#define for_in(n) for (int i = 0; i < n; ++i)
#define si(x) int(x.size())
#define all(x) (x).begin(), (x).end()
#define pb(...) push_back(__VA_ARGS__)
#define X first
#define Y second
using namespace std;

int f(vector<vector<int>>& a, vector<vector<int>>& d, int p, int q) {
  if (p == 0) return a[q][p];
  if (d[q][p] != -1) return d[q][p];
  int ret = a[q][p];
  if (p > 0) ret += f(a, d, p - 1, !q);
  if (p > 1) ret = max(ret, a[q][p] + max(f(a, d, p - 2, q), f(a, d, p - 2, !q)));
  d[q][p] = ret;
  return ret;
}
int main() {
  fastio;
  int t, n;
  cin >> t;
  while (t--) {
    cin >> n;
    vector<vector<int>> a(2, vector<int>(n)), d(2, vector<int>(n, -1));
    for (int i = 0; i < 2; ++i)
      for (auto& j : a[i]) cin >> j;
    cout << max(f(a, d, n - 1, 0), f(a, d, n - 1, 1)) << "\n";
  }
}