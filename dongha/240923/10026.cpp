#include <algorithm>
#include <climits>
#include <iostream>
#include <stack>
#include <vector>
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

int n;
string board[105];
bool vis[105][105][2];

// option 매개변수를 통해 색약이 아닌 사람이 탐색할 때와 색약인 사람이 탐색할 때를 나눔
// 특별한 발상이 필요하진 않고 문제의 조건 그대로 케이스를 잘 나누어서 탐색하는 문제
void dfs(int x, int y, bool option) {
  for (int dir = 0; dir < 4; ++dir) {
    int nx = x + "2101"[dir] - '1', ny = y + "1210"[dir] - '1';
    if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
    if (vis[nx][ny][option]) continue;
    if (!option) {
      if (board[x][y] == 'B' && board[nx][ny] != 'B')
        continue;
      else if (board[x][y] != 'B' && board[nx][ny] == 'B')
        continue;
    } else if (board[x][y] != board[nx][ny])
      continue;
    vis[nx][ny][option] = 1;
    dfs(nx, ny, option);
  }
}
int main() {
  fastio;
  cin >> n;
  int ans1 = 0, ans2 = 0;
  for (int i = 0; i < n; ++i) cin >> board[i];
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (!vis[i][j][0]) {
        vis[i][j][0] = 1;
        dfs(i, j, 0);
        ans1++;
      }
      if (!vis[i][j][1]) {
        vis[i][j][1] = 1;
        dfs(i, j, 1);
        ans2++;
      }
    }
  }
  cout << ans2 << " " << ans1 << "\n";
}