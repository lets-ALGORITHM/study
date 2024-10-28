n = int(input())
cnt = 0
num = 666
temp = 0

while 1:
  temp = num

  while (temp != 0):
    if temp % 1000 == 666: # 1000으로 나눴을 때의 나머지가 666이면 종말의 수
      cnt += 1 # 카운트하고 반복문 탈출
      break
    temp //= 10 # 나머지가 666이 아닐 경우, 10으로 나눠주어 자릿수를 하나 낮춰보고 다시 나머지 연산을 해본다.

  if cnt == n: # 입력값과 카운트값이 같으면 출력
    print(num)
    break

  num += 1 # 아니라면 num에 1을 더해주어 다시 반복문 실행
