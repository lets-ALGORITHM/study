#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
#define PATH "/Users/leedongha/Downloads/PS/input.txt"
#define L_PATH "input.txt"
#define fastio cin.tie(0)->sync_with_stdio(0);
#define rep(n) for (int i = 0; i < n; ++i)
#define si(x) int(x.size())
#define all(x) (x).begin(), (x).end()
#define pb(...) push_back(__VA_ARGS__)
#define X first
#define Y second
#define ROOT 1
#define INF 0x3f3f3f3f
using namespace std;
using ll = long long;
using TP = tuple<int, int, int>;
using P = pair<int, int>;

int main() {
  fastio;
  freopen(PATH, "r", stdin);
  int n;
  cin >> n;
  vector<int> a(n);
  for (auto& i : a) cin >> i;
  sort(all(a));
  int ans = -INF;
  do {
    int tot = 0;
    for (int i = 0; i < n - 1; ++i) tot += abs(a[i] - a[i + 1]);
    ans = max(ans, tot);
  } while (next_permutation(all(a)));
  cout << ans << "\n";
}