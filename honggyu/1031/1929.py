import math

start,end=map(int,input().split())

sqrt_value=int(math.sqrt(end))+1

li=[1]*(end+1)
li[1]=0


for i in range(2,sqrt_value):
    for j in range(i*2,end+1,i):
        li[j]=0

for i in range(start,end+1):
    if li[i]==1:
        print(i)