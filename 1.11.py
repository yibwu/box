def foo(n):
    if n < 3:
        return n
    else:
        return foo(n - 1) + 2 * foo(n - 2) + 3 * foo(n - 3)


def bar(n):
    return bar_iter(n, 0, 2, 1, 0)
        

def bar_iter(n, count, fn1, fn2, fn3):
    if n < 3:
        return n
    elif n - count < 3:
        return fn1
    else:
        return bar_iter(n, count + 1, fn1 + 2 * fn2 + 3 * fn3, fn1, fn2)


def func(n):
    if n < 3:
        return n
    else:
        count = 0
        fn, fn1, fn2, fn3 = 0, 2, 1, 0
        while count < n - 2:
            fn = fn1 + 2 * fn2 + 3 * fn3
            fn3 = fn2
            fn2 = fn1
            fn1 = fn
            count += 1
        return fn


n = 5 

ret = foo(n)
print(ret)

ret = func(n)
print(ret)

ret = bar(n)
print(ret)
