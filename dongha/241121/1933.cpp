#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
#define PATH "/Users/leedongha/Downloads/PS/input.txt"
#define L_PATH "input.txt"
#define fastio cin.tie(0)->sync_with_stdio(0);
#define rep(n) for (int i = 0; i < n; ++i)
#define si(x) int(x.size())
#define all(x) (x).begin(), (x).end()
#define pb(...) push_back(__VA_ARGS__)
#define X first
#define Y second
#define ROOT 1
#define INF 0x3f3f3f3f
using namespace std;
using ll = long long;
using TP = tuple<int, int, int>;
using P = pair<int, int>;

int n;

// (x좌표, 높이)를 오름차순으로 저장하는 우선순위 큐
priority_queue<P, vector<P>, greater<P>> pq;
// 해당 x좌표에서 높이 변화 체크가 끝났는지 보는 set 자료구조
set<int> dup;
// key: 높이, val: 해당 높이 건물의 갯수
map<int, int> hSet;

// 왼쪽 x좌표부터 순회하되 건물이 시작하는 지점과 끝나는 지점을 구분하면서 map에 특정 높이 건물의 갯수가 몇개인지
// 갱신하는 게 기본 골자
int main() {
  fastio;
  freopen(PATH, "r", stdin);
  cin >> n;
  for (int l, h, r, i{}; i < n; ++i) {
    cin >> l >> h >> r;
    /*
    높이가 음수면 건물이 시작하는 상황, 즉 map에 집어넣는 상황
    왜 이렇게 했냐면 동일한 l에 대해서 여러 높이가 시작할 수 있는데, 이 때 변화량은 가장 높은 높이로 나와야 함
    예를 들어 이전 높이가 1이고, x좌표 3에서 높이 7, 15, 20인 건물이 시작하면 높이 20인 건물이 가장 먼저 와야 함
    x좌표 변화 중복 체크를 dup으로 하니까 7이 먼저 나오면 x좌표 3에 체크를 하니까 높이 15, 20은 출력이 안 됨
    따라서 음수로 집어넣으면 -20, -15, -7 순이므로 절댓값이 가장 큰 높이가 먼저 오는 효과
    */
    pq.push(P(l, -h));
    /*
    높이가 양수면 건물이 끝나는 상황, 즉 map에서 빼는 상황
    동일한 r에 대해서 여러 높이가 끝난다면, 거꾸로 가장 낮은 높이가 먼저 나와야 함
    */
    pq.push(P(r, h));
  }

  // 현재 높이, 초깃값은 0으로 시작
  int he = 0;

  // x좌표가 오름차순으로 정렬되어 있음
  while (!pq.empty()) {
    auto [x, h] = pq.top();
    pq.pop();
    // 높이가 음수면, 즉 건물이 시작하는 상황이면
    if (h < 0) {
      h *= -1;
      // 높이 h인 건물 1개 추가
      hSet[h]++;
      // 높이가 양수면, 즉 건물이 끝나는 상황이면
    } else {
      // 높이 h인 건물 1개 감소
      hSet[h]--;
      // 0개가 됐다면 집합에서 아예 없애주기 위해서 삭제함
      if (hSet[h] == 0) hSet.erase(h);
    }

    // 현재 map이 비었다면 건물이 모두 끝난 상황, 따라서 높이는 0으로 변화함
    if (hSet.empty()) {
      he = 0;
      cout << x << " " << he << " ";
      // 해당 좌표에선 출력 끝났다는 중복 체크
      dup.insert(x);
    }
    // *prev(hSet.end()).X는 현재 map에 존재하는 건물 중 가장 큰 높이
    // 그게 내 현재 높이와 다르다 == 건물의 높이가 변화했다
    // 동일 x좌표에 대해 여러 높이가 있을 때 중복 출력을 막기 위해 추가 체크
    else if (he != (*prev(hSet.end())).X && !dup.contains(x)) {
      // 현재 높이 갱신하고 변화한 높이 출력, x좌표 중복 체크
      he = (*prev(hSet.end())).X;
      cout << x << " " << he << " ";
      dup.insert(x);
    }
  }
}