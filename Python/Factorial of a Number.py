num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Sorry, Factorial doesn't exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(2, num+1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)
