"""Given a string, return a new string made of every other
char starting with the first, so "Hello" yield "Hlo"."""


def string_bits(str):
    return str[::2]


# Alternative approach:
# def string_bits(str):
#     result = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result = result + str[i]

# word = "123456789"
# print(word[::1])
# print(word[::2])
print(string_bits("123456789"))
print(string_bits("Hello"))
