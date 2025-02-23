/*
BFS 문제, 늘 먹던 맛 익숙한 맛.
*/

# include <iostream>
# include <vector>
# include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int start, target;
    cin >> start >> target;

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v); // u와 치환 가능한 문자 리스트에 v 추가
        graph[v].push_back(u); // v와 치환 가능한 문자 리스트에 u 추가
    }

    vector<int> distance(n + 1, -1); // 각 문자까지의 치환 횟수를 저장할 벡터
    queue<int> q; // BFS 할라고 만든 큐

    distance[start] = 0;
    q.push(start);

    while(!q.empty()) {
        int current = q.front(); // 큐의 맨 앞에 있는 문자를 선택해주자.
        q.pop(); // 그리고 선택한 문자를 큐에서 제거한다.
        
        if (current == target) { // 목표 문자에 도달할 경우 탐색을 종료한다.
            break;
        }

        // 현재 문자와 치환 가능한 모든 문자를 탐색해주자.
        for (int next : graph[current]) {
            if (distance[next] == -1) { // 아직 방문하지 않은 문자라면,
                distance[next] = distance[current] + 1; // 다음 문자까지의 치환 횟수는 현재 문자까지의 치환 횟수 + 1.
                q.push(next); // 다음 문자를 큐에 삽입하고 탐색 ㄱㄱ
            }
        }
    }

    cout << distance[target] << "\n";
    return 0;
}
