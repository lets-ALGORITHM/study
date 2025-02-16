/*
DP로 누적합을 구하고, 이걸 나중에 더해주는 문제.
*/

# include <iostream>
# include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    // 누적합을 기록하기 위해 DP 테이블을 만들어주자.
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

    // 누적합을 구하는데, 이 때 겹치는 영역인 dp[i - 1][j - 1]을 한 번 빼준다.
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1];
        }
    }

    while (m--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        int ans = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1];

        cout << ans << "\n";
    }

    return 0;
}
