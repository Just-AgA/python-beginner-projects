#Check if two strings are balanced,meaning if s1 is included in s2
s1 = "Yn"
s2 = "PYnative"


def check_balance(s1, s2):
    #setup a boolean first
    balanced = True

    for char in s1:
        if char in s2:
            continue
        else:
            balanced = False

    return balanced

print(check_balance(s1, s2))
