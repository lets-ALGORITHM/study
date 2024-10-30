x, y = map(int, input().split())
extent = 250 * 250 / 2

if (x, y) == (0, 0): # [Case 1]
    print('125.00 125.00')

elif 0 < x < 125 and y == 0: # [Case 2-1]
    temp = 250 - extent / (250 - x)
    print(f'{temp:.2f} {250 - temp:.2f}')

elif x >= 125 and y == 0: # [Case 2-2]
    print(f'0.00 {extent / x:.2f}')

elif x == 0 and 0 < y < 125: # [Case 3-1]
    temp = 250 - extent / (250 - y)
    print(f'{250 - temp:.2f} {temp:.2f}')

elif x == 0 and y >= 125: # [Case 3-2]
    print(f'{extent / y:.2f} 0.00')

elif x > 0 and y > 0: # [Case 4]
    temp = 250 - extent / max(x, y)
    if x > y:
        print(f'0.00 {temp:.2f}')
    else:
        print(f'{temp:.2f} 0.00')

# 참고 자료와 함께 설명
# Mathematics, Implementation, Geometry, Case Work
