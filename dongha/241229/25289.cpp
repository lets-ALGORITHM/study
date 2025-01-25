#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
using TPi = tuple<int, int, int>;
using Pi = pair<int, int>;

int n, ans, A[100005];
int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> A[i];

  for (int d = -99; d <= 99; ++d) {
    auto solve = [&](int d) -> int {
      int ret = 0;
      // dp[x] = 마지막 숫자가 x인 가장 긴 등차 부분 수열의 길이
      vector<int> dp(101);
      for (int i = 0; i < n; ++i) {
        if (A[i] - d > 0 && A[i] - d < 101) {
          dp[A[i]] = dp[A[i] - d] + 1;
          ret = max(ret, dp[A[i]]);
        } else {
          dp[A[i]] = 1;
        }
      }

      return ret;
    };

    ans = max(ans, solve(d));
  }

  cout << ans << "\n";
}