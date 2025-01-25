import sys

input=sys.stdin.readline

N=int(input())
table=[0]*(N+1)
# [0] 제외

table[0]=1
table[1]=1

for i in range(2,N+1):
    if (table[i-2]+table[i-1])>15746:
        
        table[i]=(table[i-2]+table[i-1])%15746
    else:
        table[i]=table[i-2]+table[i-1]
    

print(table[N]%15746)