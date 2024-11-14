import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    n=int(input())
    li=[]
    li.append([0 for _ in range(n)])
    dp=[]
    dp.append([0 for _ in range(n)])
    
    for _ in range(2):
        li.append(list(map(int,input().split())))
        dp.append([0]*n)

    dp[1][0]=li[1][0]
    dp[2][0]=li[2][0]
    for j in range(1,n):
        for i in range(3):
            # i : 리스트 선택   j : 항목 선택
            if i==0:
                dp[i][j]=max(dp[1][j-1],dp[2][j-1])
            elif i==1:
                dp[i][j]=max(dp[2][j-1],dp[0][j-1])+li[i][j]
            elif i==2:
                dp[i][j]=max(dp[1][j-1],dp[0][j-1])+li[i][j]


    print(max(dp[0][n-1],dp[1][n-1],dp[2][n-1]))