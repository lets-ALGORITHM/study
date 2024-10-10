from collections import deque
n = int(input()) # TC 개수

'''
[BFS] - 최소 횟수로 목표 지점까지 이동
'''

# 나이트가 현재 위치에서 이동 가능한 칸(시계 방향)
dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(n):
    l = int(input()) # 체스판 한 변의 길이
    startX, startY = map(int, input().split()) # 시작 지점
    targetX, targetY = map(int, input().split()) # 목표 지점
    
    visited = list([0] * l for _ in range(l)) # 방문했는지 체크
    q = deque()
    q.append((startX, startY, 0)) # (현재 x, 현재 y, 현재 이동 횟수)
    ans = float('inf')
    
    while q:
        x, y, cnt = q.popleft()
        
        if visited[x][y]: # 이미 방문한 칸이면 다음 q의 원소로 패스
            continue
        
        if x == targetX and y == targetY: # 목표 지점 도달했으면
            ans = cnt # ans에 현재 이동 횟수 기록
            break
        
        visited[x][y] = 1 # 아직 방문하지 않았고 & 목표 지점 아니라면
        for i in range(8): # 나이트 8방향으로 이동시키기
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < l and 0 <= ny < l: # 이동하려는 위치가 체스판 안의 위치이면
                q.append((nx, ny, cnt+1)) # deque에 추가
    
    print(ans)