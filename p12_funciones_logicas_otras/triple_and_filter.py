# triple_and_filter
# Write a function called triple_and_filter. This function should accept a list of numbers, filter out every number that is not evenly divisible by 4 (i.e., filter out numbers that do not divide by 4 with a remainder of zero), and return a new list where every remaining number is tripled.
#
# '''
# triple_and_filter([1,2,3,4]) # [12]
# triple_and_filter([6,8,10,12]) # [24,36]
# '''


def triple_and_filter(lista):
    return [elemento * 3 for elemento in lista if elemento % 4 == 0]


def triple_and_filter2(lst):
    return list(map(lambda x: x * 3, filter(lambda x: x % 4 == 0, lst)))


print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))
