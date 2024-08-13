import sys

n = int(input())
nList = []
nAns = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nList.append([x, y])
# print(nList)

#그리디?
#1앞에 수 중심으로 오름차순
#2 뒤에 수 중심으로 오름차순
# 하고나서 겹치는 구간은 고려하고.
nList.sort(key = lambda x : (x[1], x[0]))
# print(nList)

cnt, end = 0, -1

for start_t, end_t in nList:
    # if start_t == end_t == end:

    if start_t >= end: #겹치지 않는 다음 회의
        cnt+=1
        end = end_t #유효한, 강의시간 확정된 수업의 종료시간 고정

print(cnt)
