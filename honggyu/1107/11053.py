import sys

input=sys.stdin.readline

N=int(input())

table=list(map(int,input().split()))
ans=[1]*N


for i in range(N):
    for j in range(i):
        if table[i]>table[j] and ans[i]<=ans[j]:
            ans[i]=ans[j]+1

print(max(ans))