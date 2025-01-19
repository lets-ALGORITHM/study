# 브루트포스..?
# 모든 위치에 대해, 기어 2개를 겹쳐보자
# 겹치는 구간에서 기어 2개가 모두 이(2)라면 제외
# 충돌이 없으면, 가장 왼쪽과 가장 오른쪽을 찾아 가로폭을 구하자
# 최소값을 계속 갱신하여 최종 결과로 출력

gearA = list(map(int, list(input().strip())))
gearB = list(map(int, list(input().strip())))

lenA = len(gearA)
lenB = len(gearB)

result = lenA + lenB

for shift in range(-lenB + 1, lenA):
    flag = False
    for i in range(lenB):
        pos = i + shift
        if 0 <= pos < lenA:
            if gearA[pos] == 2 and gearB[i] == 2:
                flag = True
                break
    
    if not flag:
        left = min(0, shift)
        right = max(lenA - 1, shift + lenB - 1)
        width = right - left + 1
        if width < result:
            result = width

print(result)
