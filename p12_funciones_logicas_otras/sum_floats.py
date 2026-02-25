# Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

def sum_floats(*valores):
    return sum(valor for valor in valores if type(valor) == float)


print(sum_floats(1.5, 2.4, 'awesome', [], 1))
print(sum_floats(1, 2, 3, 4, 5))
