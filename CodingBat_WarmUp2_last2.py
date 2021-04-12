"""Given a string, return the count of the number of times
that a substring length 2 appears in the string and also 
as the last 2 chars of the string, so "hixxxhi" yields 1
(we won't count the end substring)."""

# last2('hixxhi') --> 1
# last2('xaxxaxx') --> 1
# last2('axxxaaxx') --> 2

# Steps:
# len(str) > 2 otherwise count = 0
# last2 = str[-2:]
# counter = 0
# look in range from len(str[:-2])
# check for substring len(2)

# word = "Hello"
# print(word[1:3])


def last2(str):
    if len(str) < 2:
        return 0

    last2 = str[-2:]
    counter = 0

    for i in range(len(str[:-2])):
        sub = str[i : i + 2]
        if sub == last2:
            counter += 1
    return counter


print(last2("axxaxxaxx"))
