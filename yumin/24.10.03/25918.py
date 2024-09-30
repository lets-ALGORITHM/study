# 정상적으로 문자열이 입력되었을 경우에는, '('와 ')'의 갯수가 동일해야 함.
# 그렇다면, '('와 ')'를 각각 1과 -1로 바꾸었을 때, 문자열의 값을 모두 더하면 0이 나와야 함.
# 1 또는 -1을 순차적으로 더한 값들 중에서(+ 절댓값), 그 중 최댓값이 문제에서 요구하는 최소 일수를 나타냄.

n = int(input()) # 문자열의 길이 입력
s = input() # 문자열 입력

nums = [] # 문자열을 1 또는 -1로 변환한 결과를 저장할 리스트

for i in s: # 문자열 확인
    if i == '(': # 문자열의 값이 '('라면
        nums.append(1) # 1을 nums 리스트에 추가
    else: # 문자열의 값이 ')'라면
        nums.append(-1) # -1을 nums 리스트에 추가

cnt = [] # nums의 합을 순차적으로 기입할 리스트

if sum(nums) != 0: # nums 값들의 합이 0이 아니라면
    print(-1) # -1을 출력
else: # nums 값들의 합이 0이라면
    sum_nums = 0 # nums 값들의 합을 순차적으로 할당할 변수
    for i in nums: # nums의 값들을 확인
        sum_nums += i # sum_nums 변수에 nums의 값을 더함
        cnt.append(abs(sum_nums)) # 그 절댓값을 cnt 리스트에 추가
    print(max(cnt)) # 반복문 이후, cnt 리스트의 최댓값을 출력

# Greedy, Ad-hoc
