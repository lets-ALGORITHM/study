#include <bits/stdc++.h>

/*
매 순간 남아있는 지뢰 중에서 가장 파워가 큰 지뢰를 폭발시키는 게 최솟값을 찾는 방법이다.
가장 파워가 큰 지뢰 말고 다른 지뢰를 폭발시켰는데 그게 최솟값이라고 하자.
4 5 1 과 같이 있을 때 4를 먼저 터뜨리고 5를 터뜨리면 2번인데 실제 최솟값은 5를 터뜨렸을 때의 1번이므로 모순이다.
따라서 가장 큰 지뢰를 폭발시켰을 때가 최솟값인 걸 증명할 수 있다.
(지뢰 파워, 지뢰 번호)를 배열에 담고 파워가 큰 순으로 정렬해서 아직 터지지 않은 지뢰면 터뜨린다.
지뢰를 터뜨리는 것은 재귀로 구현했다.'
시간복잡도는 O(NlgN)이다.
*/
int n;
void bomb(int i, std::vector<int>& a, std::vector<bool>& check) {
  check[i] = true;
  if (i > 0 && a[i - 1] < a[i] && !check[i - 1]) bomb(i - 1, a, check);
  if (i < n - 1 && a[i + 1] < a[i] && !check[i + 1]) bomb(i + 1, a, check);
}
int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  std::cin >> n;
  std::vector<int> a(n);
  std::vector<std::pair<int, int>> o(n);
  std::vector<bool> check(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> a[i];
    o[i] = {-a[i], i};
  }
  sort(o.begin(), o.end());
  std::vector<int> ans;

  for (int i = 0; i < n; ++i) {
    auto [_, idx] = o[i];
    if (check[idx]) continue;
    ans.push_back(idx + 1);
    bomb(idx, a, check);
  }

  std::sort(ans.begin(), ans.end());
  for (auto i : ans) std::cout << i << "\n";
}