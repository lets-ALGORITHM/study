
import copy



N=int(input())
li=list(map(int,input().split()))


answer=0
# 시작 정하기 / i로 시작
for i in li:
    li02=copy.deepcopy(li)
    li02.remove(i)
    # i로 시작

    temp=i

    # 누적 길이
    finallength=0
    while li02:
        # 부분 길이
        maxlength=0



        save=None
        # 리스트 탐색
        for j in li02:

            # 부분 길이 임시 저장
            
            if abs(temp-j)>maxlength:
                maxlength=abs(temp-j)
                save=j

        # finallength+=(abs(temp-save))
        if save==None:
            save=li02[0]
        finallength+=maxlength
        temp=save


        li02.remove(temp)
    
    if answer<finallength:
        answer=finallength

print(answer)


