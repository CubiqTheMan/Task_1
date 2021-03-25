def IsPrime(a):
    d = 2
    while d * d <= a and a % d != 0:
        d += 1
    return d * d > a
a = int(input())
if a <= 1:
    print(a, " - не простое")
elif IsPrime(a) == True:
    print(a, " - простое")
else:
    print(a, " - не простое")