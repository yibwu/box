def pascal_triangle(n, result):
    if n == 1:
        result.append([1])
        return [1] 
    else:
        arr_n1 = pascal_triangle(n - 1, result)
        arr_n = [1] * n 
        for i, _ in enumerate(arr_n[1: -1]):
            arr_n[i + 1] = arr_n1[i] + arr_n1[i + 1]
        result.append(arr_n)
        return arr_n


n = 10
result = []
pascal_triangle(n, result)
for r in result:
    print(r)
