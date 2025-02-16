/*
빡구현 문제에 그만 정신을 잃고 말았읍니다..
*/

# include <iostream>
# include <vector>
# include <string>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<string> grid(N);
    for (int i = 0; i < N; i++) {
        cin >> grid[i];
    }

    // 해변은 인접한 두 칸 중 한쪽은 땅('#'), 한쪽은 물('.')인 경우의 변의 길이
    int coast = 0;

    /*
    grid 전체를 순회하면서, 각 칸이 땅인 경우 인접한 칸이 물이면 해변 길이를 증가시킨다.
    문제는 지도의 단위가 육각형이라는 점..
    행에 따라 인접한 칸의 위치가 달라지므로, 짝수 행과 홀수 행의 좌표 배열을 다르게 처리해주자.
    */
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            // 현재 칸이 땅일 경우에만 주변을 조사한다.
            if (grid[r][c] == '#') {
                // 짝수 행인 경우
                if (r % 2 == 0) {
                    // 아래 변수는 육각형의 6 방향을 나타내준다.
                    int dr[6] = {-1, -1, 0, 0, 1, 1}; // 행의 변화량
                    int dc[6] = {-1, 0, -1, 1, -1, 0}; // 열의 변화량

                    // 인접 칸의 행과 열의 좌표를 계산해주자.
                    for (int i = 0; i < 6; i++) {
                        int nr = r + dr[i], nc = c + dc[i];

                        // 인접 칸이 grid의 범위를 벗어나면 건너뛰고,
                        if (nr < 0 || nr >= N || nc < 0 || nc >= M)
                            continue;
                        // 인접 칸이 물이면 해변 길이 1 증가.
                        if (grid[nr][nc] == '.')
                            coast++;
                    }
                }
                // 홀수 행인 경우
                else {
                    // 홀수 행의 경우 타일이 밀려있으므로, 6 방향을 살짝 다르게 설정해주자.
                    int dr[6] = {-1, -1, 0, 0, 1, 1};
                    int dc[6] = {0, 1, -1, 1, 0, 1}; 

                    // 짝수 행 계산이랑 똑같이 ㄱㄱ
                    for (int i = 0; i < 6; i++) {
                        int nr = r + dr[i], nc = c + dc[i];
                        if(nr < 0 || nr >= N || nc < 0 || nc >= M)
                            continue;
                        if(grid[nr][nc] == '.')
                            coast++;    
                    }
                }
            }
        }
    }

    cout << coast;
    return 0;
}
