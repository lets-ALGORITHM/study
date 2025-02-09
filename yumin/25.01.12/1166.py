# 이분 탐색

n, l, w, h = map(int, input().split())

left, right = 0.0, min(l, w, h)

for _ in range(100): # for 문을 얼마나 돌려야 할지 감이 안잡혀서 GPT한테 물어보니 100번 정도 돌리라고 했다.. 또 그렇게 했더니 풀림
    mid = (left + right) / 2
    count = (l // mid) * (w // mid) * (h // mid)

    if count >= n:
        left = mid
    else:
        right = mid

print(left)
