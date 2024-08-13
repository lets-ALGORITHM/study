#참고링크: https://ryu-e.tistory.com/40
import sys, math
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
nList = []

for _ in range(n):
    nList.append(list(map(int, sys.stdin.readline().split())))
# print(nList)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j): #매개변수는 각 국가의 좌표.
    dq = deque() #데큐사용
    dq.append((i, j))
    visited[i][j] =True
    
    union =[(i, j)] #연합된 국가 담음
    count = nList[i][j] #총 연합한 국가들의 인구수 총합
    
    while dq:
        x, y = dq.popleft()
        
        for d in range(4): 
            #상하좌우 이동하면서 인구차이 조건 충족하는 애들을 연합국가 union에 담음
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or ny < 0 or nx >= n or ny>= n: #범위 벗어나면
                continue
            if visited[nx][ny]:#이미 방문한 애들도
                continue
            #인구차이 조건: 현재 국가에서 이동 예정인 국가간의 인구차이 l이상 r이하 충족하면
                #연합에도 담고, 방문여부포함 + 그 다음을 위해 데큐에담기
            if l <= abs(nList[nx][ny] - nList[x][y]) <= r:
                union.append((nx, ny))
                visited[nx][ny] = True
                dq.append((nx, ny))

                count += nList[nx][ny]
    #데크를 다비웠다면, bfs 작업이 전부 끝났다는 것
    
    #연합에 들어간 각국가들의 좌표
        #이 작업을 꼭 해줘야함.
        #이렇게 해서 연합 인구수 리셋해줘야 그 다음날로 넘어감
    for x, y in union:
        nList[x][y] = math.floor(count / len(union))
    return len(union)

    
cnt = 0 #인구이동 발생 일수. 정답 구하기
while True: #인구이동 그만할 때까지 반복
    visited =[[0] * n for _ in range(n)]
    flag = False #인구이동 발생했는지 추적.
    
    #bfs로 모든곳 방문
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:#bfs(0,0)하면서 이미 수많은 좌표들 방문하게됨
                if bfs(i, j) >1: #연합이 2개 이상의 국가로 구성될 때, 인구 이동이 발생한 것임
                    #인구 이동이 필요한 연합이 생겼다는 뜻.
                    flag = True
    if not flag: #False면 더이상 인구이동이 발생하지 않다는 것
        break
    cnt+=1
    
print(cnt)