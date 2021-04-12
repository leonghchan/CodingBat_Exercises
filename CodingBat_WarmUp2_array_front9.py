"""Given an array of ints, return True if one of the first
4 elements in the array is a 9. The array length may be 
less than 4."""

# Notes:
# if len(nums) < 4
# return 9 in nums[0: len(nums)]
# else:
# return 9 in nums[0: 4]


def array_front9(nums):
    if len(nums) < 4:
        return 9 in nums[0 : len(nums)]
    else:
        return 9 in nums[0:4]


# Alternative approach:
# def array_front9(nums):
#     end = len(nums)
#     if len(nums) > 4:
#         end = 4
#     for i in range(end):
#         if nums[i] == 9:
#             return True
#     return False


import numpy as np

nums_1 = np.array([1, 2, 3, 4, 5, 9])
nums_2 = np.array([9, 2, 2])

print(array_front9(nums_1))
print(array_front9(nums_2))

