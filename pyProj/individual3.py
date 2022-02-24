n = 123
while n < 999:
    ol = 0
    sum = 0
    mult = 1
    r = n
    if (n > 0):
        d = n % 10
        sum = sum + d
        mult = mult * d
        n = n // 10
        d = n % 10
        sum = sum + d
        mult = mult * d
        n = n // 10
        d = n % 10
        sum = sum + d
        mult = mult * d
        n = n // 10
        if sum == mult:
            ol = 1
    if ol == 1:
        print(r)
    n = r + 1
    sum = 0
    mult = 1