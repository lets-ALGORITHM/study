# 에라토스테네스의 체

nums = [True for _ in range(1000001)]

for i in range(2, 1000001):
    if nums[i]:
        for j in range(i * 2, 1000001, i):
            nums[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    
    for i in range(2, n // 2 + 1):
        if nums[i] and nums[n - i]:
            cnt += 1
    
    print(cnt)
