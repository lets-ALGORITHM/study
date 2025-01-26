#include <bits/stdc++.h>
using i64 = long long;

/*
처음엔 (x1, y1)에서 (x2, y2)로 이동할 때의 경우의 수가 몇 개인가? 라는 문제를 푸는 것으로 생각했는데
그럼 부분 문제의 갯수가 최대 200^4개라 너무 많은데 조금 더 생각해보면 좌표의 값 자체는 중요하지 않고
시작점과 도착점의 좌표 차이만 중요하다. 따라서
f(x) = x좌표차 dx, y좌표차가 dy일 때 이동할 수 있는 경우의 수
라고 문제를 정의하면
부분 문제는 200^2개고 따라서 DP로 해결할 수 있다
최단 거리로 이동하기 위해서는 반드시 좌표차가 줄어드는 방향으로만 이동해야하고
dx나 dy가 0인 경우에는 한 쪽의 좌표차를 줄이는 경우의 수 단 1개뿐이라는 걸 생각하면 된다
*/
constexpr int M = 1e6 + 7;

i64 solve(int dx, int dy, std::vector<std::vector<i64>>& dp) {
  i64& ret = dp[dx][dy];
  if (ret != -1) return ret;
  if (dx == 0 || dy == 0)
    return ret = 1;
  else
    return ret = solve(dx - 1, dy, dp) + solve(dx, dy - 1, dp) % M;
}
int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int w, h, tx, ty;
  std::cin >> w >> h >> tx >> ty;
  std::vector dp(202, std::vector<i64>(202, -1));
  std::cout << solve(tx - 1, ty - 1, dp) * solve(w - tx, h - ty, dp) % M << "\n";
}