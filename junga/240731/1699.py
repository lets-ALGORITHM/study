n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, int(n**(1/2))+1):
    dp[i**2] = 1

for j in range(n+1):
    if dp[j] == float('inf'):
        for k in range(int(j**(1/2)), 0, -1):
            dp[j] = min(dp[j], dp[j-k**2]+1)
            # print(j, k, dp[j])
    # for j in range(i**2, n-i**2+1):
    #     print(j, dp)
    #     dp[j+i**2] = min(dp[j+i**2], dp[j]+1)

print(dp[-1])

n = int(input())

def solve(n):
    dp = [i for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, int(i**(1/2))+1):
            sqare = j**2
            if sqare > i:
                break
            dp[i] = min(dp[i], dp[i-sqare]+1)

    return dp[-1]

print(solve(n))