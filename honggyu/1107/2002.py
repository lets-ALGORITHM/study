import sys

input=sys.stdin.readline

N=int(input())
daegun=[]
youngsik=[]

for _ in range(N):
    daegun.append(input().strip())

for _ in range(N):
    youngsik.append(input().strip())


count=0
for i in range(N):
    pivot=youngsik.index(daegun[i])
    if i==0:
        continue
    
    if pivot<i:
        count+=1
        continue

    flag=True
    for j in range(i):
        if flag:
            if daegun[j] not in youngsik[:pivot]:
                count+=1
                flag=False


 
print(count)


