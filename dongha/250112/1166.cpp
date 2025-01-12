#include <bits/stdc++.h>
using i64 = long long;

/*
이분 탐색으로 최대 A를 찾기
채울 수 있는지 판정할 때 5를 2.4로 나눈다고 하면 결과값이 정수가 되어야 한다는 것에 주의하자
예를 들면 상자가 1.3개 들어간다, 이런 건 말이 안된다.
실수에서 이분 탐색을 돌리는 건 처음이라 범위 설정을 고민하다가 변수로 몇 번 돌릴지 설정했다.
소수 범위에서도 10e-9까지면 0 기준 2^30번이니까 30번 정도 더 돌리면 된다.
정수 범위까지 고려해 넉넉하게 100으로 잡았다. 한 70해도 될듯?
*/
i64 n, l, w, h;
bool ok(double mid) {
  if (mid > std::max({l, w, h})) return false;
  return i64(l / mid) * i64(w / mid) * i64(h / mid) >= n;
}
int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  std::cin >> n >> l >> w >> h;

  double lo = 0, hi = 1e9;
  int c = 70;
  while (c-- && lo < hi) {
    double mid = (lo + hi) / 2;
    if (ok(mid))
      lo = mid;
    else
      hi = mid;
  }

  std::cout << std::fixed << std::setprecision(10) << lo << "\n";
}