import sys

input=sys.stdin.readline

N=int(input())

tri=[]
ans=[]

for _ in range(N):
    tri.append(list(map(int,input().split())))

for i in range(N):
    ans.append([0]*(i+1))

ans[0][0]=tri[0][0]

for i in range(1,N):
    for j in range(i+1):
        # i 줄의 j번째
        if j==0:
            ans[i][j]=ans[i-1][j]+tri[i][j]
        elif j==i:
            ans[i][j]=ans[i-1][j-1]+tri[i][j]
        else:
            ans[i][j]=max(ans[i-1][j-1],ans[i-1][j])+tri[i][j]


print(max(ans[N-1]))


