


'''
abcd e dcba

abcd dcba

'''

sentence=input()


allcnt=int(len(sentence)/2)

cnt=0
for i in range(int(len(sentence)/2)):

    num01=i
    num02=-(i)
    num02-=1
    
    if sentence[num01]==sentence[num02]:
        cnt+=1
    else:
        break

samecnt=0
for i in range(len(sentence)-1):
    if sentence[i]==sentence[i+1]:
        samecnt+=1


if samecnt==len(sentence)-1:
    print(-1)
elif allcnt==cnt:
    print(len(sentence)-1)
else:
    print(len(sentence))

























