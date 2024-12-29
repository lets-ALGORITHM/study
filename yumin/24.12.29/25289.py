# DP 가보자구잉 ~ !!

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [0] * 101
ans = 0


for d in range(-99, 100):
    for i in range(101):
        dp[i] = 0
    
    for x in a:
        prev = x - d
        if prev < 1 or prev > 100:
            dp[x] = 1
        else:
            dp[x] = dp[prev] + 1
        
        ans = max(ans, dp[x])

print(ans)
