# 문제 요약 : 나보다 작은 상어들 중에서 제일 큰 상어를 먹어야 함
# 맨 처음 풀 때는 상어 리스트 자체를 while문 순회마다 정렬했는데, 시간초과가 나버렸다..
# 상어 마릿수는 200,000까지 가능하기 때문에, 따로 스택을 만들어서 상어의 사이즈를 확인해야 한다.
# 먹을 수 있는 상어들을 스택에 넣어두고, 나중에 꺼내먹는 구조

import sys, heapq # 스택에 있는 상어들 중 제일 큰 상어를 먹어야 하는데, GPT한테 물어보니까 힙을 쓰라고 알려줬다.
input = sys.stdin.readline

n, k, t = map(int, input().split())
sharks = list(map(int, input().split()))
sharks.sort() # 상어들을 오름차순으로 정리한다.

heap = [] # 힙 생성
index = 0 # 상어 리스트에서 상어들을 확인하기 위한 변수

for _ in range(k): # k만큼 반복
    while index < n and sharks[index] < t: # while문으로 내가 먹을 수 있는(t보다 작은) 상어들을 전부 스택에 담아준다.
        heapq.heappush(heap, -sharks[index]) # 최대 힙을 만들어주기 위해 상어 값을 음수로 넣어준다.
        index += 1 # 다음 상어를 확인하기 위해 index에 1을 더해준다.
    if not heap: # 먹을 상어가 없다면(상어들이 t보다 크다면)
        break # 반복문 탈출

    t += -heapq.heappop(heap) # 음수로 넣어진 상어 값을 다시 양수로 반환하여 t에 더해준다.

print(t)

# 파이썬에서 힙은 기본적으로 최소 힙의 형태를 가진다.
# 최대 힙을 만들어주기 위해선, 값들을 음수로 넣어주면 된다.
# 그리고 값을 다시 꺼낼 때 양수로 변환해주면 최대 힙 완성
