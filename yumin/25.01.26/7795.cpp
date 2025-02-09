/*
나는 포인터로 풀었는데
다른 사람들은 어떻게 풀었을지..
*/

# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        vector<long long> a(n), b(m);

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        for (int i = 0; i < m; i++) {
            cin >> b[i];
        }

        sort(a.begin(), a.end()); // 원소간의 비교를 위해, 리스트를 오름차순으로 정렬한다.
        sort(b.begin(), b.end());

        int cnt = 0;
        int c2 = 0; // 포인터 변수

        /* 
        a의 원소 각각을 b의 모든 원소와 비교하여 풀 수도 있겠지만, 맨처음 파이썬으로 문제를 풀던 나는 시간초과가 나버릴 것 같아 다른 방법을 쓰기로 했다.. 그런데 C++은 될지도? 아님말고
        a의 i번째 원소를 b의 원소들과 비교하였다고 하자.
        a의 i번째 원소보다 작은 b의 원소들(잡아먹을 수 있는)이 있을 것이다.
        그렇다면, a의 (i + 1)번째 원소는 이미 'i번째 원소보다 작은 b의 원소들'을 잡아먹을 수 있으므로, 그것들과 비교하는 것을 제낄 수 있다.
        이 코드에서는 변수 c2가 포인터 역할을 하고, 변수 값을 초기화시키지 않음으로써, 이전의 원소와 비교되었던 값들의 카운트를 저장해두고 계속 활용할 수 있는 것.
        */
        for (int c1 = 0; c1 < n; c1++) {
            while (c2 < m) {
                if (a[c1] <= b[c2]) { // a의 원소가 b의 원소보다 작거나 같다면 못먹으니까
                    break; // 반복문을 탈출하자.
                } else {
                    c2++; // 아니라면 먹을 수 있으므로, 포인터에 카운트하자.
                }
            }
            cnt += c2; // 카운트한 값을 cnt 변수에 더해주자. 그런데!! c2 값은 0으로 초기화되지 않고 계속 누적되는 것이다!!
        }

        cout << cnt << "\n";
    }

    return 0;
}
