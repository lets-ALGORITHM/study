import sys

input=sys.stdin.readline

N=int(input())

house=[]

answer=[[0 for _ in range(3)]for _ in range(N)]

for _ in range(N):
    house.append(list(map(int,input().split())))



answer[0]=house[0]

for i in range(1,N):
    answer[i][0]=min(answer[i-1][1],answer[i-1][2])+house[i][0]
    answer[i][1]=min(answer[i-1][0],answer[i-1][2])+house[i][1]
    answer[i][2]=min(answer[i-1][0],answer[i-1][1])+house[i][2]


print(min(answer[N-1]))