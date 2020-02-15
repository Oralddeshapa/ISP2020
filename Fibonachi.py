def febonachi(n):
    if n <= 0:
        return
    a = 1
    b = 0
    while n > 0:
        yield a
        a, b = a+b, a
        n -= 1


a = int(input())
for x in febonachi(a):
    print(x)