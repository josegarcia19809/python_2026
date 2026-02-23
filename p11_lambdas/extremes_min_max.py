# Extremes Exercise - Using Min and Max
# Write a function called extremes  which accepts an iterable.
# It should return a tuple containing the minimum and maximum elements.  For example:
#
# extremes([1,2,3,4,5])  # (1, 5)
#
# extremes((99,25,30,-7))  # (-7, 99)
#
# extremes("alcatraz")  #( 'a', 'z')
#
# REMEMBER, RETURN A TUPLE!!!

def extremes(lista):
    return min(lista, key=lambda n: n), max(lista, key=lambda n: n)


def extremes2(nums):
    return min(nums), max(nums)


print(extremes([1, 2, 3, 4, 5]))
print(extremes((99, 25, 30, -7)))
print(extremes("alcatraz"))
