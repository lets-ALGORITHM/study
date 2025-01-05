# 그리디임
# 지뢰를 최소한의 수만큼만 터뜨리려면, 주변(양 옆)보다 크거나 같은 특정 지뢰를 터뜨리면 됨

# Q. 주변 지뢰는 자신의 충격 강도를 초과하는 지뢰의 폭발에만 터지는데, 왜 크거나 같은 지뢰를 터뜨려야 함?
# A. 큰 지뢰만 터뜨리게 되면, 자신과 같은 충격 강도를 가진 지뢰는 해결하지 못하게 됨
# EX. 2 2 2 2 2 2 2 2
# 위의 입력 예시를 해결하기 위해서는, 무조건 양 옆보다 크거나 같은 지뢰를 터뜨려야 하는 것

import sys
input = sys.stdin.readline

n = int(input())
p = [int(input()) for _ in range(n)]

if n == 1: # 만약 지뢰가 1개밖에 없다면, 그 지뢰만 터뜨리면 됨
    print(1) # 첫 번째 지뢰만 터뜨리자

else: # 지뢰가 1개 이상인 경우
    if p[0] >= p[1]: # 첫 번째 지뢰의 경우, 비교 대상이 두 번째 지뢰 밖에 없으므로 따로 조건문을 설정해주자
        print(1) # 만약 첫 번째 지뢰가 그리디 조건에 부합한다면, 출력
        
    for i in range(1, n - 1): # 첫 번째 지뢰 이후부터는, for문을 돌려주자
        if p[i - 1] <= p[i] >= p[i + 1]: # 그리디 조건에 부합한다면
            print(i + 1) # 출력
    
    if p[n - 2] <= p[n - 1]: # 마지막 지뢰도, 비교 대상이 이전 지뢰 밖에 없으므로, 따로 조건문을 설정해주자
        print(n) # 그리디 조건에 부합하면, 출력