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

/*
스위핑 알고리즘의 대표적 문제이다. 겹치는 선을 어떻게 처리하는지가 핵심인데,
직관적으로 생각했을 때 겹치는 선들은 구간의 시작과 끝을 체크하면 된다. 이를
위해서 주어지는 선들을 시작점이 작은 순으로 반드시 정렬할 필요가 있다. 그래야
순회할 때 겹치는 선들끼리 붙어있기 때문이다. 겹치는 선에서 가장 작은 좌표와 가장
큰 좌표를 동시에 가져가면서 갱신한다. 다음 선이 해당 선과 겹치지 않고 아예
벗어나 있으면 새로운 선이다. 반복문 내부에서 cx, cy는 현재 시작 좌표와 끝 좌표를
의미하고 nx와 ny는 다음 선의 시작 좌표의 끝 좌표를 의미한다. nx가 cy보다 크면
현재 선의 끝점보다 다음 선의 시작점이 더 뒤에 있다는 뜻이므로 새로운 선이다.
겹치면 cy만 ny로 갱신해준다.
*/
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