# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.

# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'


def front3(str):
    str2 = []
    for i in str:
        str2.append(i)
    if len(str2) <= 3:
        return str * 3
    else:
        str3 = str2[0] + str2[1] + str2[2]
        return str3 * 3


# print(front3("Chocolate"))
