# Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'


def front_back(str):
    str2 = []
    temp = ""
    for i in str:
        str2.append(i)
    if len(str2) > 1:
        temp = str2[0]
        str2[0] = str2[len(str2) - 1]
        str2[len(str2) - 1] = temp
        return "".join(str2)
    else:
        return str


# print(front_back('a'))
