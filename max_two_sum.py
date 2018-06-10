def max_two_sum1(x, y, z):
    if x < y and x < z:
        return y + z
    if y < x and y < z:
        return x + z
    if z < x and z < y:
        return x + y


# beautiful and elegant
def max_two_sum2(x, y, z):
    if x < y and x < z:
        return y + z
    else:
        return max_two_sum2(y, z, x)


if __name__ == '__main__':
    x, y, z = 2, 1, 3
    ret = max_two_sum1(x, y, z)
    print(ret)
    ret = max_two_sum2(x, y, z)
    print(ret)
