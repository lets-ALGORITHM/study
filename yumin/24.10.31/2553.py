n = int(input())
num = 1

for i in range(2, n + 1): # 팩토리얼 연산
    num *= i

num = str(num) # 팩토리얼 연산을 한 값을 문자열로 변경, 파이썬은 자료형을 다루기가 쉬워서 괜찮은데.. 다른 언어는 모르겠음

for j in num[::-1]: # 뒷자리부터 체크
    if j == '0': # 0이면 패스
        pass
    else:
        print(j) # 0이 아니면 출력
        break

# Mathematics, Number Theory
