#include <algorithm>
#include <iostream>
#include <numeric>
#define PATH "/Users/leedongha/Downloads/PS/input.txt"
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

// dp[n] = n을 제곱수의 합으로 표현할 때 항의 최소개수
int dp[100005];
int main() {
  fastio;
  int n;
  cin >> n;
  fill(dp, dp + 100005, INF);
  dp[0] = 0;
  dp[1] = 1;
  for (int i = 2; i <= n; ++i) {
    // 반복문 조건에서 i - j * j >= 0이 항상 보장됨. 시간복잡도 O(n√n)
    for (int j = 1; j * j <= i; ++j) {
      dp[i] = min(dp[i], dp[i - j * j] + 1);
    }
  }
  cout << dp[n] << "\n";
}