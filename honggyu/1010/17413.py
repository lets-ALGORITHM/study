from collections import deque

queue=deque()

qstr=input()


ans=[]

flag=False
for i in qstr:
    
    if i=='<':
        while queue:
            ans.append(queue.pop())
        flag=True
        ans.append(i)
    elif i=='>':
        flag=False
        ans.append(i)
    elif flag:
        ans.append(i)
    elif i==' ':
        while queue:
            ans.append(queue.pop())
        ans.append(i)
    else:
        queue.append(i)

while queue:
    ans.append(queue.pop())

for i in ans:
    print(i,end='')
    
    