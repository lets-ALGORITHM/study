import sys
input = sys.stdin.readline
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
x, y, n = map(int, input().split())
now = [500, 500, 0]
x, y = x+500, y+500
puddles = []
road = [[0] * 1001 for _ in range(1001)]
for _ in range(n):
    a, b = map(int, input().split())
    road[a+500][b+500] = -1
q = deque()
q.append(now)

def solve():
    while q:
        xx, yy, dist = q.popleft()
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if nx == x and ny == y:
                return dist+1
            if 0 <= nx <= 1000 and 0 <= ny <= 1000 and road[nx][ny] == 0:
                road[nx][ny] = dist+1
                q.append([nx, ny, dist+1])

print(solve())
