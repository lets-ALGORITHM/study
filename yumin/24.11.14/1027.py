# 시간 제한이 2초, 진하게 느껴지는 브루트포스의 냄새..
# 건물과 건물 사이의 기울기에 관한 문제
# 두 점 사이를 지나는 직선의 방정식 공식을 썼다.

n = int(input())
buildings = list(map(int, input().split()))
cnt = 0

for i in range(n):
    temp = n - 1 # 기준이 되는 건물을 제외한 수에서 하나씩 차감할 예정

    for j in range(i + 1, n): # 기준이 되는 건물의 오른쪽 부분 (기울기 증가를 체크)
        for k in range(i + 1, j):
            if buildings[k] - buildings[i] >= ((buildings[j] - buildings[i]) / (j - i)) * (k - i): # 건물과 건물 사이에, 더 큰 건물이 있다면
                temp -= 1 # 다른 건물이 안보이니까 차감
                break
        
    for j in range(0, i): # 기준이 되는 건물 왼쪽 부분 (기울기 감소를 체크)
        for k in range(j + 1, i):
            if buildings[k] - buildings[j] >= ((buildings[i] - buildings[j]) / (i - j)) * (k - j): # 건물과 건물 사이에, 더 큰 건물이 있다면
                temp -= 1 # 다른 건물이 안보이니까 차감
                break
    
    cnt = max(temp, cnt) # 제일 많이 보이는 건물의 수 골라내기

print(cnt)
