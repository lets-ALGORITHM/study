
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
            return
        

        else:
            for k in range(8):
                if 0<=i+dn[k]<l and 0<=j+dm[k]<l:
                    if table[j+dm[k]][i+dn[k]]==0:
                        table[j+dm[k]][i+dn[k]]=cnt+1
                        queue.append([i+dn[k],j+dm[k],cnt+1])

          


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
    ans=bfs()
    
    

'''
1
8
0 0
7 7
'''