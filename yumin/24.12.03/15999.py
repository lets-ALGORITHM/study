# 진짜 존나 느린 파이썬.. 시간초과가 계속 나길래 PyPy로 제출했더니 맞았다.
# 격자의 색깔은 B, W 둘 중 하나이므로, 격자판의 경우의 수는 2 ** (n * m)이다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
frame = [list(input().strip()) for _ in range(n)]

dx = [-1, 0, 1, 0] # 상 하
dy = [0, 1, 0, -1] # 좌 우

cnt = 0

for i in range(n):
    for j in range(m):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx >= 0 and nx < n and ny >= 0 and ny < m: # 격자의 범위 내에서
                if frame[i][j] != frame[nx][ny]: # 현재 자리를 기준으로 상, 하, 좌, 우 중 색깔이 다른 격자가 있다면
                    cnt += 1 # 체크
                    break

print(pow(2, n * m - cnt, 1000000007))
