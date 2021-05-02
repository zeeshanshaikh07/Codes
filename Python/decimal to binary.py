def converttoBinary(n):
    if n > 1:
        converttoBinary(n//2)
    print(n % 2, end=" ")

dec = 4
converttoBinary(dec)
print()