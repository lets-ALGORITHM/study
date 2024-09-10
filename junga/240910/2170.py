import sys
input = sys.stdin.readline

n = int(input())
dots = []
for _ in range(n):
    dots.append(list(map(int, input().split())))
dots.sort(key=lambda x:(x[1], x[0]), reverse=True)

lines = []
for i in range(n):
    if not lines or dots[i][1] < lines[-1][0]:
        lines.append(dots[i])
        continue
    if lines[-1][1] > dots[i][1] and lines[-1][0] < dots[i][0]:
        continue
    else:
        lines[-1][0] = dots[i][0]

ans = 0
for line in lines:
    ans += line[1] - line[0]
print(ans)
