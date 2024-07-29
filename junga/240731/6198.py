import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
buildings = []
ans = 0
for _ in range(n):
    buildings.append(int(input()))
s = []

for building in buildings:
    while s and s[-1] <= building: # 나보다 낮거나 같은 건물은 어차피 나 이후의 건물 못 봄
        s.pop()
    s.append(building)
    ans += len(s)-1 # s : 나(building)를 볼 수 있는 건물 리스트

print(ans)