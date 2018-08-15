def fast_expt(base, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        t = fast_expt(base, n // 2)
        return t * t
    else:
        return base * fast_expt(base, n - 1)


def fast_expt2(base, n):
    return expt_iter(base, n, n, 1) 
    

def expt_iter(base, n, old, produce):
    if n == 0:
        return produce
    elif n % 2 == 0:
        if produce == 1:
            return expt_iter(base, n - 1, old, base)
        else:
            return expt_iter(base, n // 2, old, produce * produce)
    else:
        if n == 1 and old % 2 == 0:
            return expt_iter(base, n - 1, produce * produce)
        else:
            return expt_iter(base, n - 1, base * produce)


def foo(base, n):



base = 2
for n in range(11):
    ret = fast_expt(base, n)
    print(n, ret)

for n in range(11):
    ret = fast_expt2(base, n)
    print(n, ret)
