from random import randint, shuffle


def direct(length: int)->list:
    array = []
    for i in range(length):
        array.append(i)
    return array


def reverse(length: int)->list:
    array = direct(length)
    array.reverse()
    return array


def random(length: int)->list:
    array = direct(length)
    shuffle(array)
    return array
