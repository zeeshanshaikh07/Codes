n = int(input())

for i in range(n):
    z = str(input())
    l = len(z)
    if l > 10:
        print(z[0], end='')
        print(l-2, end='')
        print(z[l-1])
    else:
        print(z)

