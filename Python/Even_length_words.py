def printwords(s):
    s = s.split(' ')

    for word in s:
        if len(word) % 2 == 0:
            print(word)


s = 'i am zeeshan'
printwords(s)
