"""Given a string and a non-negative int n, return a larger
string that is n copies of the original string."""


def string_times(str, n):
    return str * n


# Alternative approach:
# def string_times(str, times):
#     result = ""
#     for i in range(n): # range(n) is [0, 1, 2, ..., n-1]
#         result = result + str

# print(string_times("ha", 3))

