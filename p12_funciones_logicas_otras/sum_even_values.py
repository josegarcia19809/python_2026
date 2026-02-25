# Write a function called sum_even_values. This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, the function should return 0.  To be clear, it accepts all the numbers as individual arguments!
#
# sum_even_values(1,2,3,4,5,6) # 12
# sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0

def sum_even_values(*numeros):
    if len(numeros) == 0:
        return 0
    elif len(numeros) >= 1:
        return sum([num for num in numeros if num % 2 == 0])
    return 0


def sum_even_values2(*args):
    return sum(arg for arg in args if arg % 2 == 0)


print(sum_even_values(1, 2, 3, 4, 5, 6))
print(sum_even_values(4, 2, 1, 10))
print(sum_even_values(1))
