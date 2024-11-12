# 이 문제 고른 사람 누구임 ?

# 사용 가능한 문자의 종류가 100가지
# 문자의 인덱스(순서)를 리스트에 매핑하고, 해당 값을 나중에 점화식에 넣어주자.

# 브루트포스 같은 방식으로는 시간초과 때문에 풀 수 없는 문제.
# 문자를 대입하는 방식을 찾아가면 점화식이 하나 나온다.
# ex. code = abcd
# len이 1인 password는 a b c d / 4번의 시도 횟수 이내에 찾을 수 있다.
# len이 2인 password는 aa ab ac ad ba bb bc bd ca cb cc cd da db dc dd / (4 * 1) + (4 * 2)번의 시도 횟수 이내에 찾을 수 있다.
# 문자의 맨 마지막 부분에 해당하는 위치는 password의 각 문자열의 순서 값을 곱해주면 된다.

# 암호의 앞부분에서부터 계산하다가 막혀서 뒷부분에서부터 계산했다.

code = input()
password = input()

sequence = [0] * 400 

for i, c in enumerate(code, start = 1): # enumerate 함수로 문자의 순서를 편하게 가져오고, 리스트에 매핑한다.
    sequence[ord(c)] = i

control = 1
ans = 0
cnt = len(code)

for c in reversed(password): # 점화식 계산, 연산마다 % 900528을 넣어주어야 출력초과가 나지 않는다.
    ans = (ans + control * sequence[ord(c)]) % 900528
    control = (control * cnt) % 900528

print(ans)
