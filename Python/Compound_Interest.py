def compound(p, t, r):
    print("The principal is", p)
    print("The time period is", t)
    print("The rate of interest is", r)

    ci = p * (1 + r / 100) ** t

    print("The Simple Interest is", ci)

compound(1200, 2, 5.4)
