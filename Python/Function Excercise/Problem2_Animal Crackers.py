def animal_cracker(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]

wordlist = animal_cracker("Crazy cats")
print(wordlist)