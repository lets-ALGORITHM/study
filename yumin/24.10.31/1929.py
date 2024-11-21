m, n = map(int, input().split())

for num in range(m, n + 1):
    cnt = 0

    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                cnt += 1
                break

        if cnt == 0:
            print(num)

# 이 문제는 그냥 풀 경우 시간초과가 뜸
# m부터 n까지의 수가 굉장히 많을 수 있기 때문에, 계산을 확실하게 줄여야 함
# num이 소수인지를 판별할 때, 2부터 num까지 수를 for문으로 다 돌려서 확인하는데
# 이렇게 하면 시간초과
# 약수들은 대칭으로 이루어져 있음 (12 = 1, 2, 3, 4, 6, 12)
# 12를 예로 들었을때 1, 2, 3으로 나누어지는지만 확인하면 나머지는 확인할 필요가 없음
# 1, 2, 3과 4, 6, 12를 가르는 기준은 12의 제곱근(루트)