"""Given a string and a non_negative int n, we'll say that
the front of the string is the first 3 chars, or whatever
is there if the string is less than length 3. Return n copies
of the front."""


def front_times(str, n):
    if len(str) < 3:
        return str[:n] * n
    else:
        return str[:3] * n


# Alternative approach 1:
# def front_times(str, n):
#     if len(str) >= 3:
#         front = str[0:3]
#         return front*n
#     else:
#         front = str[:len(str)]
#         return front*n

# Alternative approach 2:
# def front_times(str, n):
#     front_len = 3
#     if len(str) < front_len:
#         front_len = len(str)
#     front = str[:front_len]

#     result = ""
#     for i in range(n):
#         result = result + front
#     return result

print(front_times("Beautiful", 5))
