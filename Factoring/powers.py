def pow3(x, n):
    r = 1
    while n:
        if n % 2 == 1:
            r *= x
            n -= 1
        x *= x
        n /= 2
    return r


m = pow3(2, 3774688)
print(m)