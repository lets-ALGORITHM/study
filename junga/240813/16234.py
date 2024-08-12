import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0

def check(x1, y1, x2, y2):
    if l <= abs(ground[x1][y1] - ground[x2][y2]) <= r:
        return True
    return False

def solve():
    global ans
    while True:
        cont = False
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    temp = []
                    temp_sum = ground[i][j]
                    q = deque()
                    q.append((i, j))
                    temp.append([i, j])
                    visited[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and check(x, y, nx, ny):
                                cont = True
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                temp.append([nx, ny])
                                temp_sum += ground[nx][ny]
                    if len(temp) == 1:
                        continue
                    mean = temp_sum // len(temp)
                    for c in temp:
                        ground[c[0]][c[1]] = mean
        if cont:
            ans += 1
            continue
        else:
            return ans
print(solve())   
                