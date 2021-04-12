"""CodingBat Warmup-1 Exercises"""

# near_hundred: Give an int n, return True if it is within 10 of 100 or 200.


def near_hundred(n):
    return (abs(100 - n) <= 10 or abs(200 - n) <= 10)

# pos_neg: Given 2 int values, return True if one is negative and one is positive.
#          Except if the parameter "negative" is True, then return True only if both
#          are negative.


def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))

# not_string: Given a string, return a new string where "not" has been added to the
#             front. However, if the string already begins with "not", return the
#             string unchanged.


def not_string(str):
    if len(str) >= 3 and ("not" in str[:3]):
        return str
    else:
        return "not " + str

# missing_char: Given a non-empty string and an int n, return a new string where the
#               char at index n has been removed. The value of n will be a valid
#               index of a char in the original string (i.e. n will be in the range
#               0..len(str)-1 inclusive).


def missing_char(str, n):
    if str and n < len(str):
        return str[:n] + str[n+1:]
    else:
        return "Invalid arguments."

# front_back: Given a string, return a new string where the first and last chars have
#             been exchanged. (e.g. 'code' --> 'eodc', 'a' --> 'a').


def front_back(str):
    if len(str) > 1:
        str = str[-1] + str[1:-1] + str[0]
        return str
    else:
        return str

# front3: Given a string, we'll say that the front is the first 3 chars of the string.
#         If the string length is less than 3, the front is whatever is there. Return
#         a new string which is 3 copies of the front.
#         front3('Java') --> 'JavJavJav'
#         front3('ab') --> 'ababab'


def front3(str):
    if len(str) < 3:
        front = str[0:len(str)]
    else:
        front = str[0:3]
    return front*3


print(front3('ab'))
# s = 'bossa'

# print(s[0:3])
