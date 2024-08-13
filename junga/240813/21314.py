string = list(input())
length = len(string)
def m(n):
    return "1"+"0" * (n-1)
def mk(n):
    return "5"+"0" * n

ans_max, ans_min = "", ""
idx = 0
while idx < length:
    if string[idx] == "M":
        temp = 0
        while idx < length:
            if string[idx] == "K":
                idx += 1
                temp *= -1
                break
            idx += 1
            temp += 1
        if temp >= 0:
            if idx == length:
                ans_max += "1" * temp
            else:
                ans_max += m(temp)
        else:
            ans_max += mk(-temp)
    else:
        ans_max += "5"
        idx += 1

idx = 0
while idx < len(string):
    if string[idx] == "M":
        temp = 0
        while idx < len(string):
            if string[idx] == "K":
                break
            idx += 1
            temp += 1
        ans_min += m(temp)
    else:
        ans_min += "5"
        idx += 1

print(ans_max)
print(ans_min)