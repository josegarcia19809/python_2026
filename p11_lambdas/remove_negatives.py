def remove_negatives(numeros):
    return list(filter(lambda numero: numero >= 0, numeros))


print(remove_negatives([-1, 3, 4, -99]))
print(remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
print(remove_negatives([50, 60, 70]))
