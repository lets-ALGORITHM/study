import sys
input = sys.stdin.readline

'''
[구현]
1. 답 = 각 가게와 동근이와의 최단거리 합
2. 동근이는 블록을 시계방향 또는 반시계방향 두 가지로만 이동 가능
3. 그래서 시계방향으로 돌 때와 반시계방향으로 돌 때 중 더 짧은 거리를 답에 더하면 됨
4. 시계방향으로 돌 때의 동근<->가게 거리 측정 방법
4.1. (0,0)을 기준점으로 잡고 시계방향으로 돌기 시작할 것
4.2. 시계방향으로 돌 때의 거리 = abs(동근이까지 시계방향으로 도달 거리 - 가게까지 시계방향으로 도달 거리)
5. 반시계방향으로 돌 때의 동근<->가게 거리 = (0,0)부터 한 바퀴 도는 거리 - 시계방향으로 돌 때의 거리
'''

width, height = map(int, input().split())
total = width*2 + height*2 # (0,0)부터 한 바퀴 도는 거리
n = int(input())
stores = []
ans = 0

def clockwise(line:int, dist:int): # (0,0)을 기준점으로 잡고 시계방향으로 돌 때의 거리
    if line == 1:
        return dist
    elif line == 2:
        return width + height + (width-dist)
    elif line == 3:
        return width*2 + height + (height-dist)
    elif line == 4:
        return width + dist

for _ in range(n):
    line, dist = map(int, input().split())
    stores.append([line, dist])
    
my_line, my_dist = map(int, input().split())
my_cdist = clockwise(my_line, my_dist) # 동근이까지 시계방향으로 도달 거리

for store in stores:
    store_cdist = clockwise(store[0], store[1]) # 가게까지 시계방향으로 도달 거리
    cdist = abs(my_cdist-store_cdist) # 시계방향으로 돌 때의 동근<->가게 거리
    ans += min(cdist, total-cdist) # 시계방향 동근<->가게 거리, 반시계방향 동근<->가게 거리 비교
    
print(ans)