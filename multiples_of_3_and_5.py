# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000


def multiples_of_3_or_5(total):

    nums = []

    for i in range(total):
        if (i % 3 == 0) | (i % 5 == 0):
            nums.append(i)
    return sum(nums)

# Printed sum of multiples 3 and 5 below 1000
multiples_of_3_or_5(1000)