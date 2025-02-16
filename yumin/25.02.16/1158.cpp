/*
자료구조
*/

# include <iostream>
# include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    // 1번 부터 n번까지 사람 번호를 저장하자.
    vector<int> people;
    for (int i = 1; i <= n; i++) {
        people.push_back(i);
    }

    // 결과 저장용 리스트와 현재 제거할 위치의 인덱스 변수 생성.
    vector<int> res;
    int idx = 0;

    while (!people.empty()) {
        // 원형 구조이므로, 현재 인덱스에서 (k - 1)만큼 이동한다. 
        idx = (idx + k - 1) % people.size();
        // 제거된 사람의 번호를 결과에 저장하고, 해당 사람을 리스트에서 제거하자.
        res.push_back(people[idx]);
        people.erase(people.begin() + idx);
    }

    // 파이썬이 그립습니다..
    cout << "<";
    for (int i = 0; i < res.size(); i++) {
        cout << res[i];
        if (i != res.size() - 1) {
            cout << ", ";
        }
    }
    
    cout << ">";

    return 0;
}
