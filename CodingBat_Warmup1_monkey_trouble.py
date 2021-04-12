"""We have two monkey, a and b, and the parameters a _smile
 and b_smile indicate if each is smiling. We are in trouble 
 if they are both smiling or if neither of them is smiling.
 Return True if we are in trouble."""


def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)


# Alternative approach 1:
# def monkey_trouble(a_smile, b_smile):
#     if a_smile and b_smile:
#         return True
#     elif not a_smile and not b_smile:
#         return True
#     else:
#         return False

# Alternative approach 2:
# def monkey_trouble(a_smile, b_smile):
#     return (a_smile == b_smile)

print(monkey_trouble(True, False))
