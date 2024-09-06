import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
costs = []
for _ in range(m):
    costs.append(list(map(int, input().split())))
    
'''
[MST]
1. 모든 컴퓨터들을 최소 비용으로 연결해야 함 == 모든 노드들을 최소 비용으로 연결 => MST
'''

costs.sort(key=lambda x:x[2]) # 최소 비용인 간선부터 조회해서 노드 연결해야 하므로, 비용 기준 오름차순 정렬

root = [i for i in range(n+1)] # parent[i] : i의 부모 노드
ans = 0

def find_root(a): # 노드 a의 루트 노드를 찾는 함수
    if a == root[a]: # 노드 a의 루트 노드가 자기 자신이라면
        return a # 자기 자신 return
    root[a] = find_root(root[a]) # 자기 자신이 아니라면, a의 루트 노드의 루트 노드를 재귀를 통해 찾고 찾아 결국 a의 진짜 루트 노드 찾기
    return root[a]

def union(a, b): # 노드 a, b를 연결해주는 함수
    root_a, root_b = find_root(a), find_root(b)
    # 단, 연결해줄 때 노드 a, b의 루트 노드 중 노드 번호가 더 작은 것을 루트 노드로 지정
    # why?) 그냥 꼬이지 않게 하기 위헤
    if root_a > root_b:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
 
for a, b, cost in costs:
    if find_root(a) != find_root(b): # 노드 a, b의 루트 노드가 같지 않다면(== 서로 연결되어 있지 않다면)
        union(a, b) # 연결해준다!
        ans += cost # 연결하는 데에 든 비용을 정답에 더해준다
        # 미리 간선들을 가중치 오름차순으로 정렬해두었으므로, 자동으로 최소비용으로 노드들을 연결하게 된다

print(ans)