/*
맨 처음에는 그래프인가 했는데 이게 대체 무엇인가 보니.. 애드 혹.
'#'가 있는 칸들을 전부 조사하고, 행/열의 범위를 구하여 정사각형의 위치를 구한다.
그리고 정사각형 각 변들의 가운데 좌표들을 구해주고.. '.'가 있는지 확인해주면 되는 문제.
*/

# include <iostream>
# include <vector>
# include <string>
# include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    /*
    top은 '#'가 등장하는 가장 작은 행 번호
    bottom은 '#'가 등장하는 가장 큰 행 번호
    left는 '#'가 등장하는 가장 작은 열 번호
    right는 '#'가 등장하는 가장 큰 열 번호

    min과 max 함수를 이용하여, 정사각형 네 모서리의 위치를 확인하자.
    */
    int top = n, bottom = -1, left = m, right = -1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '#') {
                top = min(top, i);
                bottom = max(bottom , i);
                left = min(left, j);
                right = max(right, j);
            }
        }
    }

    /*
    정사각형 각 변의 가운데 좌표 또한 구해주자.
    */
    int mid_row = (top + bottom) / 2;
    int mid_col = (left + right) / 2;

    /*
    각 변의 가운데 좌표를 확인해서, '.'가 있으면 해당되는 문자열을 출력시켜주자.
    */
    if (grid[top][mid_col] == '.')
        cout << "UP\n";
    else if (grid[bottom][mid_col] == '.')
        cout << "DOWN\n";
    else if (grid[mid_row][left] == '.')
        cout << "LEFT\n";
    else if (grid[mid_row][right] == '.')
        cout << "RIGHT\n";

    return 0;
}
