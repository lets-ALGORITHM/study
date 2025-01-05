# 빡구현 문제

import sys
input = sys.stdin.readline

p, m = map(int, input().split())

players = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    players.append((l, n))

rooms = []

for player_level, player_name in players:
    assigned = False

    for room in rooms:
        base_level = room['base_level']
        cnt = len(room['players'])
        
        if cnt < m and (base_level - 10 <= player_level <= base_level + 10):
            room['players'].append((player_level, player_name))
            assigned = True
            break
    
    if not assigned:
        new_room = {
            'base_level': player_level,
            'players': [(player_level, player_name)]
        }
        rooms.append(new_room)

for room in rooms:
    cnt = len(room['players'])
    
    if cnt == m:
        print("Started!")
    else:
        print("Waiting!")
    
    room['players'].sort(key=lambda x: x[1])
    for level, name in room['players']:
        print(level, name)
