/*
그리디 문제
던진 사거리의 최대값과 (던지는 사람의 위치 + 사거리)를 비교하여 지속적으로 갱신시켜주면 된다.
*/

# include <iostream>
# include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<long long> position(n);

    for (int i = 0; i < n; i++) {
        cin >> position[i];
    }

    // n이 1인 경우에는 게임을 조용히 끝마칠 수 있다.
    if (n <= 1) {
        cout << "권병장님, 중대장님이 찾으십니다\n";
        return 0;
    }

    vector<long long> ranges(n - 1);
    
    for (int i = 0; i < n - 1; i++) {
        cin >> ranges[i];
    }

    long long max_range = 0;

    // 사거리의 최댓값이 현재 수류탄을 던지는 사람의 위치보다 크거나 같다면, 최댓값과 (위치 + 사거리) 값 중 큰 값으로 최댓값을 갱신해주어 수류탄이 최대 어디까지 던져질 수 있는지를 확인할 수 있다.
    for (int i = 0; i < n - 1; i++) {
        if (max_range >= position[i]) {
            max_range = max(max_range, position[i] + ranges[i]);
        }
    }

    // 던진 사거리의 최댓값이 제일 마지막 사람의 위치보다 크면 성공, 작다면 실패.
    if (max_range >= position[n - 1]) {
        cout << "권병장님, 중대장님이 찾으십니다\n";
    } else {
        cout << "엄마 나 전역 늦어질 것 같아\n";
    }

    return 0;
}
