#include <algorithm>
#include <iostream>
#include <vector>
#define fastio cin.tie(0)->sync_with_stdio(0);
#define for_in(n) for (int i = 0; i < n; ++i)
#define si(x) int(x.size())
#define all(x) (x).begin(), (x).end()
#define pb(...) push_back(__VA_ARGS__)
#define X first
#define Y second
#define ROOT 1
#define INF 0x3f3f3f3f
using ll = long long;
using namespace std;

int main() {
  fastio;
  int n, x, y;
  cin >> n;
  vector<pair<int, int>> a;
  for (int i = 0; i < n; ++i) {
    cin >> x >> y;
    a.pb({x, y});
  }
  sort(all(a));
  auto [cx, cy] = a[0];
  ll ans = 0;
  for (int i = 1; i < n; ++i) {
    auto [nx, ny] = a[i];
    if (nx > cy) {
      ans += 1ll * cy - cx;
      cx = nx;
      cy = ny;
    }
    if (ny > cy)
      cy = ny;
  }

  ans += cy - cx;
  cout << ans << "\n";
}