# import sys
# sys.setrecursionlimit(10**6)

# N=int(input())

# li=[]
# for _ in range(N):
#     li.append(int(input()))


# minlength=1000000000
# for i in range(N-1):
#     if li[i+1]-li[i]<minlength:
#         minlength=li[i+1]-li[i]

# width=li[-1]-li[0]



# # 약수 구하기
# def get_divisors(n):
#     divisors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             divisors.append(i)
#     return divisors




# while True:
#     flag=False
#     for i in range(N-1):
#         if (li[i+1]-li[i])%minlength!=0:
#             flag=True
#     if flag:
#         divisors=get_divisors(minlength)
#         minlength/=divisors[1]
#     else:
#         print(int((li[-1]-li[0])/minlength-1-N+2))
#         break

'''

2 4 10

3 12 27

3
2
3
4

'''





N=int(input())

li=[]
for _ in range(N):
    li.append(int(input()))

minlength=1000000000




templist=[]
for i in range(N-1):
    temp=li[i+1]-li[i]
    if temp not in templist:
        templist.append(temp)

width=li[-1]-li[0]



import math
from functools import reduce

def gcd_of_list(numbers):
    return reduce(math.gcd, numbers)

result = gcd_of_list(templist)


print(int((li[-1]-li[0])/result-1-N+2))







