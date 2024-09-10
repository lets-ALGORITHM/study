import sys
input = sys.stdin.readline

ans = 0
n, m = map(int, input().split())
journey = list(map(int, input().split()))

prices = [[0, 0, 0] for _ in range(n+1)]
for i in range(1, n):
    prices[i] = list(map(int, input().split()))

frequency = [0] * (n+1)
for i in range(m-1):
    a, b = min(journey[i], journey[i+1]), max(journey[i], journey[i+1])
    frequency[a] += 1
    frequency[b] -= 1

cumsum = 0
for i in range(1, n):
    cumsum += frequency[i]
    with_ic = cumsum*prices[i][1] + prices[i][2]
    without_ic = cumsum*prices[i][0]
    ans += min(with_ic, without_ic)

print(ans)