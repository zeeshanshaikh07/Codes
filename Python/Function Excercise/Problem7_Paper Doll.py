def paper_doll(text):
    result = ""
    for char in text:
        result += char*3
    return result
result = paper_doll("Hello")
print(result)