# 정렬을 곁들인 어지러운 그리디 문제

n = int(input())
texts = []
ans = 0

for _ in range(n):
    text = input()
    texts.append(text)

texts.sort(key = lambda x : len(x))

for i in range(n):
    text = texts[i]
    flag = False

    for j in range(i + 1, n):
        if text == texts[j][0 : len(text)]: # 이 문제의 핵심, texts[j]가 text로 시작하는(접두사) 문자열이라면 제외
            flag = True
            break
    
    if not flag: # 아니면 포함시킨다
        ans += 1

print(ans)
