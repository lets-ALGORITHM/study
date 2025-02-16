/*
열심히 브루트포스로 풀면 되는 문제.
*/

# include <iostream>
# include <queue>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    // 4와 7로 이루어진 배열을 하나 만들어주자.
    int cnt = 0;
    queue<long long> q;
    q.push(4);
    q.push(7);

    /*
    배열에서 pop을 해주고, 그 수가 a와 b 사이라면 카운트 해주자.
    그리고 그 수에 10을 곱해주고 4 또는 7을 더해주어, 4와 7로 이루어진 또다른 수를 만들어낸다.
    그 수가 b보다 작다면 조건에 부합하는 수이므로, 그 수를 다시 배열에 넣어준다.
    이 과정을 배열이 빌 때까지 반복해주면 끝.
    */
    while (!q.empty()) {
        long long num = q.front();
        q.pop();

        if (num > b)
            continue;

        if (num >= a)
            cnt++;

        long long next_num1 = num * 10 + 4;
        long long next_num2 = num * 10 + 7;

        if (next_num1 <= b)
            q.push(next_num1);
        if (next_num2 <= b)
            q.push(next_num2);
    }

    cout << cnt;
    
    return 0;
}
