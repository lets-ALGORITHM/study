/*
DP
*/

# include <iostream>
# include <vector>

using namespace std;

const long long MOD = 1000000009;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    // 입력받은 n 중에서 최댓값을 저장하고, 그 수로 DP 배열의 크기를 결정하자.
    int max_n = 0;
    vector<int> cases(t);
    for (int i = 0; i < t; i++) {
        cin >> cases[i];
        if (cases[i] > max_n)
            max_n = cases[i];
    }

    /*
    DP로 정수 i를 (1, 2, 3)의 합으로 나타내는 방법의 수를 구해야한다.
    그런데 문제에서는 순서가 다른 경우도 다른 방법으로 취급한다는 것을 조심..

    미리 0부터 max_n까지 모든 DP 값을 계산해주자.
    */
    vector<long long> dp(max_n + 1, 0);
    dp[0] = 1;
    if (max_n >= 1) dp[1] = 1; // 숫자가 1인 경우, 1 = 1
    if (max_n >= 2) dp[2] = 2; // 숫자가 2인 경우, 2 = (1 + 1) or 2
    if (max_n >= 3) dp[3] = 4; // 숫자가 3인 경우, 3 = (1 + 1 + 1) or (1 + 2) or (2 + 1) or 3

    /*
    점화식 : dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    */
    for (int i = 4; i <= max_n; i++) {
        dp[i] = ((dp[i - 1] + dp[i - 2]) % MOD + dp[i - 3]) % MOD;
    }

    for (int n : cases)
        cout << dp[n] << "\n";
    
    return 0;
}
