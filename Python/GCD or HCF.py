def computegcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd
num1 = 54
num2 = 24
print(computegcd(num1,num2))