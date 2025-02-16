/*
왠지 익숙한 덱 문제.
풍선을 터뜨리는 매 단계마다 회전시켜 다음에 터질 풍선이 항상 왼쪽에 오도록 하면 된다.
*/

# include <iostream>
# include <deque>
# include <vector>
# include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> balloons(n);
    for (int i = 0; i < n; i++) {
        cin >> balloons[i];
    }

    /*
    각 풍선을 (번호, 이동값) 튜플로 저장하고 덱에 넣어주자.
    */
    deque<pair<int, int>> dq;
    for (int i = 0; i < n; i++) {
        dq.push_back({i + 1, balloons[i]});
    }

    vector<int> res;

    while (!dq.empty()) {
        // 문제에서 제일 처음에는 1번 풍선을 터뜨린다고 했으니, 1번 풍선을 먼저 터뜨려주자.
        auto cur = dq.front();
        dq.pop_front();
        res.push_back(cur.first);

        if (dq.empty()) // 덱에 풍선이 하나도 없다면, 반복을 종료하자.
            break;

        int move = cur.second;
        int size = dq.size();

        /*
        풍선에 적힌 숫자에 따라 덱을 회전시켜 다음에 터질 풍선을 왼쪽에 오게 하자.
        풍선에 적힌 숫자(move)가 양수면 그만큼 왼쪽으로 회전시키고, 음수면 그만큼 오른쪽으로 회전시키면 된다.
        */
        if (move > 0) {
            int leftRotate = (move - 1) % size;
            rotate(dq.begin(), dq.begin() + leftRotate, dq.end());
        }
        else {
            int rightRotate = (-move) % size;
            rotate(dq.begin(), dq.end() - rightRotate, dq.end());
        }
    }

    for (int num : res)
        cout << num << " ";
    cout << "\n";

    return 0;
}
