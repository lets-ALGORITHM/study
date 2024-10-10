from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
'''
고민] 규칙 존재? 중간에서부터 제일 작은거, 제일 큰 거 순으로 append, appendleft?
=> 규칙 없음 엣지케이스 너무 많음 ㅠㅠ
==> 결국 brute force(순열 or 백트래킹 사용)
==> 근데 어차피 배열 최대 길이 8이라 모든 순열 조회해도 괜찮을 것 같아 순열 사용
'''

def calc(lst: list): # 해당 식 구하는 함수
    sum = 0
    for i in range(len(lst)-1):
        sum += abs(lst[i]-lst[i+1])
    return sum

ans = 0 # 해당 식의 최댓값 저장

for l in permutations(arr):
    ans = max(ans, calc(l)) # 최댓값 갱신

print(ans)