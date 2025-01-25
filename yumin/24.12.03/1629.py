def gang(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        exp //= 2
        base = (base * base) % mod
    return res

a, b, c = map(int, input().split())

print(gang(a, b, c))
