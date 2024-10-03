# 숫자를 위치에 맞게 배정해야 되는 문제
# 큰 수부터 해당하는 위치에 넣게 되면, 굳이 조건을 쓰지 않더라도 숫자가 알아서 위치에 맞게 배정됨
# 원래 존재하던 숫자는 기존의 숫자를 밀어내고 해당 인덱스에 위치하려 하기 때문

n = int(input())

line = list(map(int, input().split())) # 입력값
height = list(range(1, n + 1)) # 오름차순으로 숫자 배열한 리스트 생성
result = [] # 결과값을 저장할 리스트

j = -1 # 제일 큰 수부터 결과값에 넣기 위해 -1을 변수에 할당
for i in range(n):
    result.insert(line[j], height[j]) # line[j]에 해당하는 위치에 height[j] 값을 result 리스트에 삽입
    j -= 1 # j에 -1을 해줌으로써 내림차순으로 숫자를 삽입할 수 있도록 함
    print(result)

print(' '.join(map(str, result))) # 결과값 출력

# Greedy, Implementation
