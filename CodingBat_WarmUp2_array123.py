"""Given an array of ints, return True if the sequence of
numbers 1, 2, 3 appears in the array somewhere."""

# Notes
# if len(nums) < 3 return False
# for i in len(nums[:-2]):
# if nums[i: i+3] == np.array([1, 2, 3])
# return True

import numpy as np


def array123(nums):
    if len(nums) < 3:
        return False
    counter = 0
    for i in range(len(nums[:-2])):
        if (nums[i : i + 3] == np.array([1, 2, 3])).all():
            counter += 1
    return counter >= 1


# Alternative approach:
# def array123(nums):
#     for i in range(len(nums)-2):
#         if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
#             return True
#     return False


nums_1 = np.array([4, 1, 2, 3, 5])
nums_2 = np.array([2, 3, 1, 2])
print(array123(nums_1))
print(array123(nums_2))

