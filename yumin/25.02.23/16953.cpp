/*
그리디로 풀었는데 문제 알고리즘 분류를 까보니 그래프..?
*/

# include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int cnt = 0;

    while (b > a) {
        /*
        b의 가장 오른쪽 자리가 1인 경우, 오른쪽의 1을 제거하기 위해 10으로 나눠주고 연산 횟수를 1만큼 증가시켜주자.
        */
        if (b % 10 == 1) {
            b /= 10;
            cnt++;
        }

        /*
        b가 짝수인 경우, 2로 나누어주고 연산 횟수를 1만큼 증가시켜주자.
        */
        else if (b % 2 == 0) {
            b /= 2;
            cnt++;
        }

        // 위 두 개의 조건을 모두 만족하지 않는 경우에는 더 이상 변환할 수 없으니까 반복 종료.
        else {
            break;
        }
    }
    
    if (b == a)
        cout << cnt + 1 << "\n";
    else
        cout << -1 << "\n";
    
    return 0;
}
