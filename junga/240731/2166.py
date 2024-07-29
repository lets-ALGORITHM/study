import sys
input = sys.stdin.readline

n = int(input())
nodes = []
for _ in range(n):
    nodes.append(list(map(int, input().split())))
nodes.append(nodes[0])

'''
[구현] - 수학
1. '가우스의 면적 공식(신발끈 공식)' 사용하면 굉장히 쉬운 문제. 근데 이런 건 언제 배우는 거지
1.1. 가우스의 면적 공식 : 다각형의 꼭짓점 좌표들을 알면 다각형의 면적 계산 가능
1.1.1. 단 시계방향/반시계방향으로 나열해야 함
1.1.2. 변끼리 교차하지 않아야 함
'''

a, b = 0, 0 # 파란색, 초록색
for i in range(n):
    a += nodes[i][0] * nodes[i+1][1]
    b += nodes[i][1] * nodes[i+1][0]
    
ans = abs(a-b)/2
print('%0.1f' % round(ans, 1)) # 반올림처리와 소수점 한자리 무조건 표시