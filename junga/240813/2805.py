n, m = map(int, input().split())
trees = list(map(int, input().split()))

'''
[이진탐색]
1. 잘라낸 나무들의 길이가 m 이상이 되게 하는 절단기 최대 높이를 구해야 함
2. 절단기 높이는 0 이상 최대나무높이 이하 => 최대 절단기 높이를 이진탐색 이용해 계산
'''


def binary_search(max_len):
    left, right = 0, max_len
    while left <= right:
        mid = (left+right)//2
        sum = 0
        for tree in trees:
            sum += max(0, tree-mid)
        if sum >= m: # 자른 나무들의 높이 합이 m 이상이라면
            left = mid + 1 # left 갱신
        else: # 아직 자른 나무들의 높이 합이 부족하다면
            right = mid - 1 # right 갱신
    return right # left는 자른 나무들의 높이 합이 m을 만족할 때에도 +1되므로 구하고자 하는 답 초과
                 # => 따라서 right를 리턴
    
cutter = max(trees) # 최대나무높이
ans = binary_search(cutter)
print(ans)
