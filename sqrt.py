def sqrt(x, precision):
    def helper(guess, x):
        if abs(x - guess ** 2) <= precision:
            return guess
        else:
            return helper((guess + x/guess) / 2.0, x)
    return helper(1.0, x)


if __name__ == '__main__':
    cases = [0.01, 1, 4, 5, 101]
    for n in cases:
        print(sqrt(n, 10e-6))
