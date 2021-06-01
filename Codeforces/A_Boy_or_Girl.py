x = input()
def main(str):
    s = set(str)
    s = "".join(s)
    if(len(s) % 2 != 0):
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
main(x)