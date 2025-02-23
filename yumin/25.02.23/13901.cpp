/*
구현이 싫어요
*/

# include <iostream>
# include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;

    vector<vector<bool>> obstacle(r, vector<bool>(c, false));
    vector<vector<bool>> visited(r, vector<bool>(c, false));

    int k;
    cin >> k;

    for (int i = 0; i < k; i++) {
        int br, bc;
        cin >> br >> bc;
        obstacle[br][bc] = true;
    }

    int sr, sc;
    cin >> sr >> sc;

    vector<int> order(4);
    for (int i = 0; i < 4; i++) {
        cin >> order[i];
    }

    vector<pair<int, int>> deltas(5);
    deltas[1] = make_pair(-1, 0);
    deltas[2] = make_pair(1, 0);
    deltas[3] = make_pair(0, -1);
    deltas[4] = make_pair(0, 1);

    int curIndex = 0;
    int direction = order[curIndex];

    int curR = sr, curC = sc;
    visited[curR][curC] = true;

    // 로봇이 움직일 수 있는 동안 반복 ㄱㄱ
    while (true) {
        // 한 칸 이동할 다음 위치도 계산해주자.
        int nextR = curR + deltas[direction].first;
        int nextC = curC + deltas[direction].second;

        // 다음 위치가 방의 범위 내에 있고, 장애물도 없고, 아직 방문하지 않은 곳이라면 로봇이 다음 위치로 이동 쓩
        if (nextR >= 0 && nextR < r && nextC >= 0 && nextC < c && !obstacle[nextR][nextC] && !visited[nextR][nextC]) {
            curR = nextR;
            curC = nextC;
            visited[curR][curC] = true;
            continue;
        }

        // 현재 방향으로 더 이상 이동할 수 없으므로, 지정된 다음 방향을 찾아보자.
        else {
            bool moved = false; // 새로운 방향으로 이동했는지 여부를 따지는 변수

            // 새로운 방향과 위치 변수..
            for (int i = 1; i <= 4; i++) {
                int newIndex = (curIndex + i) % 4;
                int newDirection = order[newIndex];
                nextR = curR + deltas[newDirection].first;
                nextC = curC + deltas[newDirection].second;

                // 해당 위치가 로봇이 갈 수 있는 곳이라면 또 ㄱㄱ
                if (nextR >= 0 && nextR < r && nextC >= 0 && nextC < c && !obstacle[nextR][nextC] && !visited[nextR][nextC]) {
                    curIndex = newIndex;
                    direction = newDirection;
                    curR = nextR;
                    curC = nextC;
                    visited[curR][curC] = true;
                    moved = true;
                    break;
                }
            }

            // 4가지 방향으로 모두 이동할 수 없다면 반복 종료.
            if (!moved)
                break;
        }
    }

    cout << curR << " " << curC << "\n";
    return 0;
}
