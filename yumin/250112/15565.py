# 두 포인터

n, k = map(int, input().split())
dolls = list(map(int, input().split()))

start = 0
cnt = 0
min_length = float('inf')

for end in range(n):
    if dolls[end] == 1:
        cnt += 1

    while cnt >= k:
        current_length = end - start + 1
        if current_length < min_length:
            min_length = current_length
        
        if dolls[start] == 1:
            cnt -= 1
        
        start += 1

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)
