def master_yoda(text):
    wordlist = text.split()
    reverse_word_list =  wordlist[::-1]
    return ' '.join(reverse_word_list)

reverse_word_list = master_yoda('I am Home')
print(reverse_word_list)
