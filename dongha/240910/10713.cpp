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
각 구간마다 그 구간을 몇 번 이용하는지를 구하면 IC 카드를 사는 게 나은지
티켓으로 타는 게 나은지 구할 수 있다. naive하게 구간을 업데이트하면 N이 최대
10^5이므로 최악의 경우 O(NM)의 시간이 걸리므로 다른 방법이 필요하다. 누적합과
연관되어 나오는 imos법이라는 게 있는데, 구간의 처음과 끝의 변화량을 표시하고
마지막에 누적합을 구하면 O(N)으로 갱신이 완료된 최종 결과를 구할 수 있다. 예를
들어 인덱스 0~9에서 3~5 구간에는 +5, 7~9 구간에는 -3을 하는 쿼리를 날렸다고 하면
arr[3] += 5; arr[6] -= 5; arr[7] -= 3;을 해주면 배열이
0 0 0 5 0 0 -5 -3 0 0 이 되는데 이 배열의 누적합을 구하면
0 0 0 5 5 5 0 -3 -3 -3 으로 O(N)의 후처리를 통해 최종 결과를 구할 수 있다.
따라서 쿼리 하나당 구간의 시작과 끝만 업데이트 해주면 되니까 O(1)이고 후처리에
O(N)이므로 쿼리가 M개면 O(N + M)의 시간복잡도로 처리할 수 있다.
*/
int d[100005];
int main() {
  fastio;
  int n, m, pre, x, a, b, c;
  cin >> n >> m >> pre;
  for (int i = 0; i < m - 1; ++i) {
    cin >> x;
    d[min(pre, x)]++;
    d[max(pre, x)]--;
    pre = x;
  }

  ll ans = 0;
  int tot = 0;
  for (int i = 1; i < n; ++i) {
    tot += d[i];
    cin >> a >> b >> c;
    ans += 1ll * min(1ll * tot * a, 1ll * tot * b + c);
  }

  cout << ans << "\n";
}