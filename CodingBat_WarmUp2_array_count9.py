"""Given an array of ints, return the number of 9's in the array."""

# for i in nums, if i == 9 then add 1 to counter


def array_count9(nums):
    counter = 0
    for i in nums:
        if i == 9:
            counter += 1
    return counter


nums = [1, 2, 9, 9]
print(array_count9(nums))

