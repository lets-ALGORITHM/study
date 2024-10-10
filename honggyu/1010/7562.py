
from collections import deque

queue=deque()


N=int(input())


dn=[2,2,-2,-2,1,1,-1,-1]
dm=[1,-1,1,-1,2,-2,2,-2]

visited={}




def bfs():
    while queue:
        temp=queue.popleft()
        i=temp[0]
        j=temp[1]
        cnt=temp[2]
        if i==target[0] and j==target[1]:
            print(cnt)
            
            return cnt
        else:
            for k in range(8):
                if 0<=i+dn[k]<l and 0<=j+dm[k]<l:
                    if table[j+dm[k]][i+dn[k]]!=0:
                        if table[j+dm[k]][i+dn[k]]>cnt+1:
                            table[j+dm[k]][i+dn[k]]=cnt+1
                            queue.append([i+dn[k],j+dm[k],cnt+1])
                    else:
                        table[j+dm[k]][i+dn[k]]=cnt+1
                        queue.append([i+dn[k],j+dm[k],cnt+1])

                    
def bfs02():
    while queue:
        temp = queue.popleft()
        i, j, cnt = temp
        
        # 목표 위치에 도달한 경우
        if (i, j) == (target[0], target[1]):
            return cnt
        
        for k in range(8):
            ni, nj = i + dn[k], j + dm[k]
            # 인덱스 범위 확인
            if 0 <= ni < l and 0 <= nj < l:
                if (ni, nj) not in visited:  # 방문 여부 체크
                    visited.add((ni, nj))  # 방문 처리
                    queue.append([ni, nj, cnt + 1])
    
    return -1  # 목표에 도달하지 못한 경우


for _ in range(N):
    l=int(input())
    now=list(map(int,input().split()))
    target=list(map(int,input().split()))
    table=[[0 for _ in range(l)] for _ in range(l)]
    
    
    cnt=0
    # ans=dfs(now[0],now[1],0)
    # visited[(now[0],now[1])]=0


    # table[now[1]][now[0]]=0
    queue.append([now[0],now[1],0])
    ans=bfs02()
    print(ans)
    




def dfs(i,j,cnt):
    if i==target[0] and j==target[1]:
        return cnt
    
    for k in range(8):
        if 0<=(i+dn[k])<l and 0<=(j+dm[k])<l:
            dfs(i+dn[k],j+dm[k],cnt+1)








'''

2
300
0 0
0 299
300
0 0
123 123




1
4
0 0
1 2


2
4
0 0
0 0
4
1 1
1 1
'''
