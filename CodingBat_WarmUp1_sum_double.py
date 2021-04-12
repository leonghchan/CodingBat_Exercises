"""Given two int values, return their sum. Unless the two
values are the same, then return double their sum."""


def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b


# Alternative approach
# def sum_double(a, b):
#     sum = a + b
#     if a == b:
#         sum = sum * 2
#     return sum

print(sum_double(2, 2))
print(sum_double(2, 3))
