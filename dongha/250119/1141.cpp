#include <bits/stdc++.h>
using i64 = long long;

/*
사전순으로 앞에 있는 게 뒤에 있는 것의 접두사가 될 수 있다. 따라서 정렬한다.
s[i]가 문자열로 가지는 다른 단어가 존재한다면 s[i + 1]은 반드시 s[i]를 접두사로 가진다.
s[i]를 문자열로 가지는 다른 단어가 존재할 때 s[i + 1]이 s[i]를 접두사로 가지지 않는다고 가정하자.
그렇다면 s[i + 1]에 있는 문자열은 s[i]를 접두사로 가지는 문자열보다 사전순으로 앞선다는 것인데
이는 s[i] 끝에 문자를 더한 문자열로만 가능하고, 그렇다면 s[i + 1]은 s[i]를 접두사로 가지므로 모순이다.

즉 s[i]가 s[i + 1]의 접두사라면 s[i]는 반드시 빠져야 한다.
 */
int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int n;
  std::cin >> n;
  std::vector<std::string> a(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> a[i];
  }
  sort(a.begin(), a.end());
  auto ispre = [&](const std::string& a, const std::string& b) {
    int n = a.size(), m = b.size();
    if (n > m) return false;
    for (int i = 0; i < n; ++i) {
      if (a[i] != b[i]) return false;
    }
    return true;
  };

  int ans = 1;
  for (int i = 0; i < n - 1; ++i) {
    ans += !ispre(a[i], a[i + 1]);
  }

  std::cout << ans << "\n";
}