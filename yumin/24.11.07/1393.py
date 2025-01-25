def gcd(a, b): # 최대공약수 구하는 함수
    while b:
        a, b = b, a % b
    return a

def distance(x, y): # 점과 직선 사이의 거리를 구하는 함수
    return ((x - xs) ** 2 + (y - ys) ** 2) ** 0.5

xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

gcds = gcd(dx, dy)
dx, dy = dx / gcds, dy / gcds
current_xe, current_ye = xe, ye

while distance(current_xe, current_ye) > distance(current_xe + dx, current_ye + dy):
    current_xe += dx
    current_ye += dy

print(int(current_xe), int(current_ye))
