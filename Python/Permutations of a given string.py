def perm(a,l,r):
    if l==r-1:
        print(a)
    else:
        for i in range(l,r):
            x = list(a)
            temp = x[l]
            x[l] = x[i]
            x[i] = temp
            perm("".join(x),l+1,r)
            temp = x[l]
            x[l] = x[i]
            x[i] = temp
string = input("Enter a String: ")
n = len(string)
perm(string,0,n)