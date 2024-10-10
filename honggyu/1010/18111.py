
import copy

N,M,B=map(int,input().split())
# N : 세로
# M : 가로
# B : 갖고 있는 블럭 개수


tablesave=[]

for _ in range(N):
    tablesave.append(list(map(int,input().split())))

candi=[]

# 높이 후보 찾기
for i in range(N):
    for j in range(M):
        if tablesave[i][j] not in candi:
            candi.append(tablesave[i][j])

if len(candi)==1:
    print(0,candi[0])

else:
    # high은 높이
    ans=[]
    for high in candi:
        table=copy.deepcopy(tablesave)
        time=0
        
        for i in range(N):
            for j in range(M):
                # 높은 것부터 낮추기
                if table[i][j]>high:
                    gap=table[i][j]-high
                    B+=gap
                    time+=(gap*2)
                    table[i][j]=high
                # 낮은 것들 내리기
                elif table[i][j]<high:
                    B-=(high-table[i][j])
                    time+=(high-table[i][j])
                    table[i][j]=high

        
                


        if B>=0:
            ans.append([time,high])


    mintime=999999999
    highsave=[]

    for i in ans:
        if i[0]<mintime:
            if i[0]!=0:
                mintime=i[0]
                highsave=[]
                highsave.append(i[1])
        elif i[0]==mintime:
            highsave.append(i[1])

    if len(highsave)==1:
        print(mintime,highsave[0])
    else:
        print(mintime,min(highsave))












