/*
피보나치 수열을 이용한 문제 (DP)
*/

# include <iostream>
# include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> vip_seats(m);
    for (int i = 0; i < m; i++) {
        cin >> vip_seats[i];
    }

    /*
    연속된 좌석이 1개일 경우에는, 앉을 수 있는 방법은 1가지
    연속된 좌석이 2개일 경우에는, (a, b)와 (b, a) 2가지
    연속된 좌석이 3개일 경우에는, (a, b, c)와 (b, a, c)와 (a, c, b) 3가지 (두 명이 움직이고, 한 명은 가만히 있어야 하므로)
    연속된 좌석이 4개일 경우에는, (a, b, c, d)와 (b, a, c, d)와 (a, b, d, c)와 (b, a, d, c)와 (a, c, b, d) 5가지
    이거 완전 피보나치 수열..
    따라서 점화식을 만들어보면, f(k) = f(k - 1) + f(k - 2)임을 알 수 있다.
    */
    vector<long long> fib(n + 1, 0);
    fib[0] = 1;
    fib[1] = 1;

    if (n >= 2) { // n의 입력값은 1도 될 수 있으므로, 무지성으로 f(2) = 2를 해서는 안된다..
        fib[2] = 2;
    }

    for (int i = 3; i <= n; i++) { // 피보나치 수를 미리 구해두자.
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    long long ans = 1;
    int prev_vip = 0; // 직전 vip 좌석을 나타내는 변수

    for (int vip : vip_seats) {
        int length = vip - 1 - prev_vip; // vip의 바로 앞까지가 '연속되는 구간의 길이'이다.
        ans *= fib[length]; // 이미 해당 구간 길이 만큼의 피보나치 수를 구해놨으므로, 값을 꺼내서 ans에 곱해주자.
        prev_vip = vip; // 다음 vip 좌석을 확인하기 위해, 값을 갱신해주자.
    }

    int length = n - prev_vip; // 마지막 vip 좌석 다음부터 n번 좌석까지의 길이를 구해주자.
    ans *= fib[length];

    cout << ans << '\n';
    return 0;
}
