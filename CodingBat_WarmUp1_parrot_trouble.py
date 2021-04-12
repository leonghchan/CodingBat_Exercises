"""We have a loud talking parrot. The "hour" parameter is the 
current hour time in the range 0 - 23. We are in trouble if 
the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble."""


def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    else:
        return False


# Alternative approach:
# def parrot_trouble(talking, hour):
#     return ((hour < 7 or hour > 20) and talking)

print(parrot_trouble(True, 8))
print(parrot_trouble(True, 5))
