import sys
input = sys.stdin.readline

n = int(input())
jwapyo = []

for _ in range(n):
    x, y = map(int, input().split())
    jwapyo.append((x, y))

garo, sero = 0, 1 # x를 기준으로 하는 변수 / y를 기준으로 하는 변수

def count(num): # 얼마나 선분과 교차하는 지를 구하는 함수
    line = [0 for i in range(500000 * 2 + 1)]

    for i in range(num, n, 2): # 입력된 값이 가로냐 세로냐에 따라 순회가 달라진다.
        j = (i + 1) if i + 1 != n else 0 # 직각다각형은 결국 원점으로 돌아와야 완성되기 때문에, 원점과 그 이전의 점을 비교하기 위해 i가 n이 되기 이전에 0으로 만들어주자.
        a = 0 if jwapyo[i][0] != jwapyo[j][0] else 1 # 좌표의 x값이 같다면, y좌표만 확인하기 위해 a = 1으로 설정 / 좌표의 x값이 다르다면, x좌표만 확인하기 위해 a = 0으로 설정
        
        min_num, max_num = sorted([jwapyo[i][a], jwapyo[j][a]]) # 스위핑으로 교차 횟수의 최댓값을 구하기 위해서는, 작은 값에 +1을 해주고 큰 값에 -1을 해주어야 된다고 한다.
        line[min_num + 500000] += 1
        line[max_num + 500000] -= 1

    ans, temp = 0, 0
    for i in line: # 교차 횟수의 최댓값을 구해주기 위해 line에 입력된 값들을 누적합으로 구해준다.
        temp += i
        ans = max(ans, temp)
    return ans

res = max(count(garo), count(sero))
print(res)
