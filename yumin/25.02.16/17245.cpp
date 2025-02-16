/*
이분 탐색
*/

# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n));
    long long total = 0; // 전체 컴퓨터의 수
    int max_computer = 0; // grid에서 최대로 쌓인 컴퓨터 수

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            total += grid[i][j];
            max_computer = max(max_computer, grid[i][j]);
        }
    }

    /*
    절반 이상이 냉방되어야 하므로, 변수 threshold의 값을 전체 컴퓨터 수의 반을 올림한 값으로 정하자.
    그리고 이분탐색을 위해 변수 low, high를 만들고, 냉방된 컴퓨터가 threshold 이상이 되는 수를 찾아주자.
    */
    long long threshold = (total + 1) / 2;
    int low = 0, high = max_computer;
    int ans = high;

    while (low <= high) {
        int mid = (low + high) / 2;
        // mid분 후에 냉방된 컴퓨터 수를 계산해주자.
        long long cooled = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // 각 칸에서는 min(쌓인 수, mid)만큼 냉방되었다는 뜻.
                cooled += min(grid[i][j], mid);
                // 만약 목표치에 도달했다면 반복 종료.
                if (cooled >= threshold)
                    break;
            }
            if (cooled >= threshold)
                break;
        }
        // 충분한 냉방이 이루어졌다면, 더 작은 수에서도 가능한지 확인하기 위해 상한선을 낮춘다.
        if (cooled >= threshold) {
            ans = mid;
            high = mid - 1;
        }
        // 냉방된 컴퓨터 수가 threshold 미만이면, 수를 늘려주자.
        else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
