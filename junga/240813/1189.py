r, c, k = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[0] * c for _ in range(r)]
visited[r-1][0] = True
def dfs(dist, x, y):
    global ans
    if dist == k and x == 0 and y == c-1:
        ans += 1
        return
    if dist > k:
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and maps[nx][ny] != "T":
            visited[nx][ny] = True
            dfs(dist+1, nx, ny)
            visited[nx][ny] = False
if maps[0][c-1] == "T":
    print(0)
else:
    dfs(1, r-1, 0)
    print(ans)