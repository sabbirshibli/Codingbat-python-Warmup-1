# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.
#
# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True


def pos_neg(a, b, negative):
    if a <= -1 < b and negative == False:
        return True
    if b <= -1 < a and negative == False:
        return True
    if a < 0 < b and negative == True:
        return False
    if b < 0 < a and negative == True:
        return False
    if a < 0 and b < 0 and negative == True:
        return True
    if b < 0 and a < 0 and negative == False:
        return False
    else:
        return False


# print(pos_neg(-4, 5, True))
