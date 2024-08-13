import sys
input = sys.stdin.readline

sInput = list(input().rstrip())

def fMin():
    stack = []
    ans =''

    for elem in sInput:
        if elem == 'K': #K나오면 조건충족.
            if len(stack):
                ans += str(10 ** (len(stack) -1))
            ans += '5'
            stack = []
        else:
            stack.append(elem)

    if len(stack):
        ans += str(10 ** (len(stack) -1))
    
    return ans


def fMax():
    stack = []
    ans = ''
    for elem in sInput:
        if elem ==  'K':
            ans += str(5 * (10 ** len(stack)))
        else:
            stack.append(elem)
    for i in stack:
        ans += '1'
    return ans

print(fMax())
print(fMin())




# https://99uulog.tistory.com/131