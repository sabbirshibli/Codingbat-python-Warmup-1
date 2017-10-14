# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0


def diff21(n):
    if n > 21:
        return abs(21 - n) * 2
    else:
        return abs(21 - n)


# print(diff21(25))
