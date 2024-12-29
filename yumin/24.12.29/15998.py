# 하.. 이 문제 누가 골랐음 ???
# 문제에서 요구하는 최소 충전 단위는 모든 필요한 충전액의 공통된 배수여야 함
# 그렇기 때문에 gcd 함수를 통해 m을 계속 갱신시켜주어야 함

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())

limit = 9 * (10 ** 18)
flag = True # 출금이 처음인지 확인하는 boolean 변수
remains = 0 # 카카오머니 잔액
maxs = 0 # 출금 이후 남은 잔액 중 가장 큰 금액
res = 1 # 최소 충전 단위 m을 1로 초기화한 값

for _ in range(n):
    a, b = map(int, input().split())

    if res == -1: # 이미 유효한 m이 없다면, 처리를 하지 않고 넘어가자
        continue

    if a < 0 and remains < -a: # a가 출금이고, 현재 잔액으로 출금이 안되는 경우
        m = - a + b - remains # 충전에 필요한 금액은 옆의 식과 같다
        if flag: # 첫 출금인 경우
            maxs = b # 충전에 필요한 금액 m을 최소 충전 단위 res로 설정
            res = m # 첫 출금 처리를 때린다
            flag = False
        else: # 이미 최소 충전 단위가 설정되어 있는 경우
            m = gcd(res, m) # 기존의 res와 새로 계산한 m의 최대공약수를 구하자
            maxs = max(maxs, b) # 기존 최대 잔액과 새롭게 계산된 잔액 중 더 큰 것으로 갱신
            if m < maxs: # 최소 충전 단위가 최대 잔액보다 작다면 모순이므로
                res = -1 # 불가능
            else: 
                if m == 1 and b != 0: # 만약 m이 1인데 잔액 b가 0이 아니라면, 모든 돈이 1원 단위로 충전되어 출금 가능이라고 해도 b가 0이 아니기 때문에 정확히 맞출 수 없음
                    res = -1 # 불가능
                else: # 그 외의 경우에는 res를 m으로 갱신한다
                    res = min(m, limit) # 대신, 문제에서 허용하는 최대값 limit과 비교하여 더 작은 것을 유지
        remains = b # 출금 후 잔액 remains를 b로 갱신
        continue

    if remains + a != b: # 단순히 현재 잔액 remains에 a를 반영한 값이 b와 일치하는지 검사하는데, 일치하지 않는다면 모순
        res = -1 # 불가능
    else:
        remains = b # 아니라면, 잔액을 b로 갱신

print(res)
