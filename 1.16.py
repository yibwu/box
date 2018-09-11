def fast_expt(base, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        t = fast_expt(base, n // 2)
        return t * t
    else:
        return base * fast_expt(base, n - 1)


base = 2
for n in range(11):
    ret = fast_expt(base, n)
    print(n, ret)
