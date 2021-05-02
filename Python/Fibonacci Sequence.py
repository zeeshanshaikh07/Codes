def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
nterms = int(input("How many terms?"))
if nterms < 0:
    print("Enter a positive number")
else:
    print("Fibonacci Sequence")
    for i in range(nterms):
        print(fibo(i))