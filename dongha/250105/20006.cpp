#include <bits/stdc++.h>

/*
각 방마다 처음 입장한 사람의 레벨, 이름 목록 보관
들어갈 수 있는 방 찾아서 있으면 넣고 없으면 방 새로 만들어줌
*/
std::map<std::string, int> nl;
int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int n, m;
  std::cin >> n >> m;
  std::vector<int> r;
  std::vector rp(0, std::vector<std::string>());
  for (int i = 0; i < n; ++i) {
    std::string name;
    int l;
    std::cin >> l >> name;
    nl[name] = l;

    int rn = -1;
    for (int i = 0; i < r.size(); ++i) {
      if (r[i] - 10 <= l && l <= r[i] + 10 && rp[i].size() < m) {
        rn = i;
        break;
      }
    }

    if (rn == -1) {
      r.push_back(l);
      std::vector<std::string> nn = {name};
      rp.push_back(nn);
    } else {
      rp[rn].push_back(name);
    }
  }

  for (int i = 0; i < r.size(); ++i) {
    if (rp[i].size() == m)
      std::cout << "Started!\n";
    else
      std::cout << "Waiting!\n";
    std::sort(rp[i].begin(), rp[i].end());
    for (auto n : rp[i]) {
      std::cout << nl[n] << " " << n << "\n";
    }
  }
}