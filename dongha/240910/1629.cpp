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

ll mod;
ll pow(ll a, ll b) {
  ll ret = 1;
  while (b) {
    if (b % 2)
      ret = ret * a % mod;
    a = a * a % mod;
    b /= 2;
  }

  return ret;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  ll a, b;
  cin >> a >> b >> mod;
  cout << pow(a, b);
}