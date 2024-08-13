import sys

n = int(input())
# nList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nList =[]
for i in range(n):
    nList.append(list(map(int, sys.stdin.readline().split())))
    nList[i].append(i)#각 리스트의 3번째 원소는 일 수
# print(nList) 

dp = [0 for _ in range(n+1)]

#'그날 상담을 시작하는 경우'와 '그날 상담을 시작하지 않는 경우'
    #상담을 시작하면 상담이 끝난 날의 그 다음날 수익이 nList[i][1]만큼 증가
nMax = 0
for i in range(n):
    nMax = max(nMax, dp[i])

    if i+nList[i][0] > n: #T더해봤는데 전체 날짜 범위 넘어가면, 그 다음날 계산
        continue
    # '현재까지의 수익에 이번 상담의 수익을 더한 값'과 '오늘의 상담이 끝나는 시점의 수익' 중 큰 값
    dp[i +nList[i][0]] = max(nMax+nList[i][1], dp[i+nList[i][0]])

print(max(dp))

# https://dndi117.tistory.com/entry/aaa
