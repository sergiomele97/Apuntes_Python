from functools import reduce


def check_odd(number):
    if number % 2 == 0:
        return False

    return True


lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8]

lista_impares = filter(check_odd, lista_original)

print(reduce(lambda a, b: a+b, lista_impares))
