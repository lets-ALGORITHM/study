# 이분 탐색 가보자구 ~~ !!

import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.append(0)
arr.append(l)
arr.sort()

start, end = 1, l
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, len(arr)):
        if (arr[i] - arr[i - 1]) > mid:
            cnt += (arr[i] - arr[i - 1] - 1) // mid
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)
