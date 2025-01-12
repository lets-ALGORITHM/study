#include <bits/stdc++.h>

/*
소수를 몽땅 찾은 다음 브루트포스를 이용해 비교한다. 최대 100만이므로 2로 나누면 50만, 숫자 하나당 검사는 최대
O(500000)고 최대 100개 들어오므로 통과한다.
시간복잡도는 O(1000000 + TN)이다.
*/
bool notp[1000001];
int f(int n) {
  int l, r, ret = 0;
  l = r = n / 2;
  while (l > 1) {
    if (!notp[l] && !notp[r]) ret++;
    l--;
    r++;
  }

  return ret;
}
int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int t;
  std::cin >> t;

  for (int i = 2; i * i <= 1000000; ++i) {
    if (notp[i]) continue;
    for (int j = i * i; j <= 1000000; j += i) {
      notp[j] = true;
    }
  }

  while (t--) {
    int n;
    std::cin >> n;
    std::cout << f(n) << "\n";
  }
}