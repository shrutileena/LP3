def sum_series(n):
    sum = 0

    for i in range(n):
        x = n - 2*i
        if x <= 0:
            break
        else:
            sum = sum + x

    return sum

num = int(input())
res = sum_series(num)
print(res)