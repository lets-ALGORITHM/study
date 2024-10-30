# 이름만 보고 풀려했다가 크게 데인 문제.. 정답률이 낮은 이유를 알겠음
# 가로, 세로의 최댓값은 500이고, 땅의 최대 높이는 256이므로, 무지성 브루트포스가 가능함
# 블럭이 높이와 그 개수를 따로 리스트에 저장해두고, 높이 0부터 256까지 땅 평탄화를 하는 경우를 반복문으로 확인하면 된다
# 그리고 그 값들 중에서 땅의 높이는 최댓값, 걸린 시간은 최솟값을 출력하면 될 듯

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split()) # 세로 n, 가로 m, 블록 개수 b를 입력 받는다
height_of_ground = {i : 0 for i in range(257)} # 블럭의 높이와, 그 높이를 가진 블럭의 개수를 저장할 딕셔너리 생성

ground = [] # 입력받을 땅
for i in range(n): 
    temp = list(map(int, input().split())) # 입력받은 땅의 행을 리스트로 변환
    ground.append(temp) # 땅 리스트에 행을 차례대로 넣고
    for j in temp: # 각 행에서, 각각의 높이에 해당하는 값들을
        height_of_ground[j] += 1 # 딕셔너리로 카운트

height_of_ground = list(height_of_ground.items()) # 딕셔너리를 다루기 편하게 리스트로 변환

time_list = [] # 땅을 평탄화하는데 드는 시간들을 저장할 리스트

for i in range(257): # 변수 i는 현재 땅 고르기를 할 높이
    below = [(key, val) for key, val in height_of_ground if key < i and val != 0] # i를 기준으로 '블럭이 존재하고', 'i보다 높이가 낮다면' below 리스트에 할당
    above = [(key, val) for key, val in height_of_ground if key > i and val != 0] # i를 기준으로 '블럭이 존재하고', 'i보다 높이가 높다면' above 리스트에 할당
    time, block = 0, 0 # time, block 변수를 생성하고, 각각 0 값으로 초기화
    block += b # block 변수에 블럭 개수(b)를 채워준다

    for height, cnt in above: # above에 할당된 변수 (높이, 개수)를 각각 height, cnt로 설정
        time += 2 * (height - i) * cnt # 블럭을 제거하는 경우, 각 블럭 개수마다 2초가 걸린다
        block += (height - i) * cnt # 블럭을 제거하고 나면, 인벤토리에 넣는다

    for height, cnt in below: # below에 할당된 변수 (높이, 개수)를 각각 height, cnt로 설정
        time += (i - height) * cnt # 블럭을 채우는 경우, 각 블럭 개수마다 1초가 걸린다
        block -= (i - height) * cnt # 블럭을 채우고 나면, 인벤토리에서 블럭이 1개씩 사라진다

    if block < 0: # 블럭을 다 사용하고 나면
        break # 반복문 탈출
    time_list.append(time) # 땅 고르기에 사용된 시간을 저장

max_height_idx = [idx for idx, t in enumerate(time_list) if t == min(time_list)] # 가장 적게 걸린 시간들 중에서 가장 높은 높이를 할당
print(min(time_list), max(max_height_idx)) # 최소 시간과 최대 높이 출력

# Implementation, Bruteforcing
