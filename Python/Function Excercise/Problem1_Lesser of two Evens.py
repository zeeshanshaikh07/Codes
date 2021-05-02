def lesser_of_two_evens(a,b):
    if a %2 == 0 and b %2 == 0:
        #BOTH NUMBERS ARE EVEN!
        return min(a,b)
    else:
        #ONE OR BOTH NUMBERS ARE ODD!
        return max(a,b)

result = lesser_of_two_evens(1,7)
print(result)
