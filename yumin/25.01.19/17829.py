# 구현인데 상당히 풀만 했던 문제

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

while n > 1: # 행렬 크가 1 by 1이 될 때까지 반복 ㄱㄱ
    new_n = n // 2 # 풀링을 하고 나면 행렬 크기가 절반이 되므로, 절반이 된 값을 할당해 줄 변수를 만들자
    new_nums = [[0] * new_n for _ in range(new_n)] # 절반이 된 행렬도 리스트 형태로 만들어 주자
    
    for i in range(new_n): 
        for j in range(new_n):
            block = [
                nums[2 * i][2 * j], # 왼쪽 위
                nums[2 * i][2 * j + 1], # 오른쪽 위
                nums[2 * i + 1][2 * j], # 왼쪽 아래
                nums[2 * i + 1][2 * j + 1] # 오른쪽 아래
            ] # 해당 값들은 원래 행렬을 2 by 2로 쪼갠 값들
            block.sort(reverse = True) # 해당 값들을 내림차순으로 정리
            new_nums[i][j] = block[1] # 2번째로 큰 값을 풀링 이후 행렬에 넣어주자
    
    nums = new_nums # 풀링 이후의 값들을 다시 기존 변수에 재할당
    n = new_n

print(nums[0][0]) # 반복이 다 끝나고 난 다음, 값을 출력
