invoerstring = input("Vul je naam, beginstation en eindstation in.")

def code(invoerstring):
    codering = " "
    for char in invoerstring:
        codering = codering + chr(ord(char)+3)
    return codering

print(code(invoerstring))
