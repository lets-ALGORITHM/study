/*
구현과 큐 문제
C++의 방대한 코드 길이에 그만 정신을 놓아버리고 말았읍니다.
*/

# include <iostream>
# include <vector>
# include <queue>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> charge(n); // 요금 리스트
    for (int i = 0; i < n; i++) {
        cin >> charge[i];
    }

    vector<long long> weight(m); // 차량의 무게 리스트
    for (int i = 0; i < m; i++) {
        cin >> weight[i];
    }

    vector<int> parking_lot(n, 0); // 주차장을 나타낼 리스트, 0은 비어있다는 뜻이다.
    queue<int> waiting; // 주차장에 자리가 꽉 차있을 경우, 차들을 대기시키기 위한 큐

    /*
    계속 주차장의 자리를 확인해도 되지만, 조금 더 시간을 줄이기 위해 주차한 차들의 개수를 체크하는 cnt 변수를 만들었다.
    cnt 변수와 주차장의 자리를 나타내는 변수인 n이 같다면 주차장이 꽉 찼다는 뜻이기 때문에, 굳이 주차장을 순회하지 않고 바로 차를 waiting 큐에 넣어버린다는 마인드.
    */
    int cnt = 0;
    int ans = 0; // 최종 요금

    for (int i = 0; i < 2 * m; i++) {
        int car;
        cin >> car;

        if (car > 0) { // 입력 받은 차가 양수일 경우 (주차)
            if (cnt == n) { // cnt와 n이 같다면 주차장이 꽉 찼다는 의미이므로
                waiting.push(car); // 밖에서 대기시키자
            }
            else { // 비어있는 자리가 있다면
                for (int j = 0; j < n; j++) { // 주차장을 순회하자.
                    if (parking_lot[j] == 0) { // 주차장에 빈 자리가 있다면
                        parking_lot[j] = car; // 차를 주차시키자.
                        cnt++; // cnt 변수도 더해주어 주차된 차의 개수가 늘어났음을 나타내주자.
                        break;
                    }
                }
            }
        }

        else { // 입력 받은 차가 음수일 경우 (출차)
            car = -car; // car를 양수로 다시 변환해주자.
            for (int j = 0; j < n; j++) { // 주차장을 순회하자.
                if (parking_lot[j] == car) { // 차가 주차된 자리를 찾아내고
                    ans += charge[j] * weight[car - 1]; // 요금과 차량의 무게를 곱한 값을 최종 요금에 더해주자.
                    if (!waiting.empty()) { // 만약 대기열에 차가 있다면
                        parking_lot[j] = waiting.front(); // 대기열의 맨처음 차를 빈자리에 주차시키자.
                        waiting.pop(); // 대기열에서 해당 차는 삭제.
                    }
                    else { // 대기열이 없다면
                        parking_lot[j] = 0; // 그냥 빈자리로 내버려두자.
                        cnt --; // 출차했으므로 cnt 변수에서 1을 빼주자.
                    }
                    break;
                }
            }
        }
    }

    cout << ans << '\n';
    return 0;
}
