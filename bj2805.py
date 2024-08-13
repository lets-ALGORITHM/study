#시간초과
import sys

n, m = map(int, sys.stdin.readline().split())

nList =list(map(int, sys.stdin.readline().split()))
# nList.sort(reverse=True)
# print(nList)

ans = 0

nBiggest = max(nList)
start = 0

#start와 nBiggest 사이의 이분탐색.
    #서로 좁혀감.
while start <= nBiggest:
    nTree = 0 #상근이가 가져갈 나무총합
    mid = (start+ nBiggest) //2
    for elem in nList:
        if elem > mid: #중간값보다 각 나무길이가 클때
            nTree += elem - mid #각 나무길이 - 중간값을 가져갈 나무총합에 더하기
    
    #위에 작업 다 해줬는데도 아직 m길이 못맞추면
    if nTree < m:
        nBiggest = mid -1 #자르는 높이 낮추기
    else:
        ans = mid #자른 높이를 결과값에 저장하고
        start = mid +1 #자르는 높이 높힌다

print(ans)
        

    