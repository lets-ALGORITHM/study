

#01 bfs

import sys
from collections import deque

input=sys.stdin.readline

time=int(input())





dn=[1,-1,0,0]
dm=[0,0,1,-1]
q=deque()



def bfs(i,j):
    ground[j][i]=0
    q.append((i,j))

    while q:
        i,j=q.popleft()
        for k in range(4):
            ni=i+dn[k]
            nj=j+dm[k]
            if 0<=ni<N and 0<=nj<M and ground[nj][ni]!=0:
                ground[nj][ni]=0
                q.append((ni,nj))





# 그래프 만들기
for i in range(time):
    # 가로 : N / 세로 : M
    N,M,K=map(int,input().split())
    ground= [[0 for _ in range(N)]for _ in range(M)]
    
    lettuces=[]

    # (가로, 세로)
    for j in range(K):
        lettuces.append(list(map(int,(input().split()))))

    for lettuce in lettuces:
        # 세로 먼저 / 가로는 그 다음
        ground[lettuce[1]][lettuce[0]]=1




    cnt=0
    for i in range(M):
        for j in range(N):
            if ground[i][j]==1:
                cnt+=1
                bfs(j,i)
    print(cnt)

    
























# #02 

# import sys
# from collections import deque


# input=sys.stdin.readline
# time=int(input())





# for i in range(time):
#     # 가로 : N / 세로 : M
#     N,M,K=map(int,input().split())


#     lettuces=[]
#     # (가로, 세로)
#     for j in range(K):
#         lettuces.append(list(map(int,(input().split()))))
#     length=len(lettuces)


#     for k in range(length):
#         try:
#             i,j=lettuces[k]
#             for ni,nj in lettuces:
#                 if (ni==i+1 and nj==j) or (ni==i-1 and nj==j)

#         except:
#             pass


    
    

#     # i : 가로 / j : 세로
    


# def implement(i,j):
#      pass

