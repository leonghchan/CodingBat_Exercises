"""Given a non-empty string like "Code" return a string
like "CCoCodCode"."""

# grab str[:i] then add to string for i in range(len(str))


def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[0 : i + 1]
    return result


# word = "Hello"
# print(word[0:5])

print(string_splosion("Code"))

