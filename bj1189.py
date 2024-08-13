import sys

# r, c, k = map( int, sys.stdin.readline().split())

# sList = []
# for _ in range(r):
#     sList.append(sys.stdin.readline().rstrip('\n'))

# print(sList)
# nVisited = [[0 for _ in range(c)] for _ in range(r)]

R, C, K = map(int, sys.stdin.readline().split())

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

visited = [[False]*C  for _ in range(R)]

map_list = [sys.stdin.readline().strip() for _ in range(R)]

def dfs(r, c, k):
  if r == 0 and c == C-1 :
    return 1 if  k == 0 else 0

  if k == 0 :
    return 0

  result = 0
  for i in range(4) :
    ar, ac = r + dr[i], c + dc[i]
    if -1 < ar < R and -1 < ac < C and map_list[ar][ac] == '.' and not visited[ar][ac] :
      visited[ar][ac] = True
      result += dfs(ar, ac, k-1)
      visited[ar][ac] = False

  return result


visited[R-1][0] = True
print(dfs(R-1, 0, K-1))


# def dfs(x, y, cnt): #매개변수는 좌표
# while True:
    
#     for i in range():
        
