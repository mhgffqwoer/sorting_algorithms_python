def quick(array: list)->None:
    if len(array) > 1:
        x = array[0]
        low = [elem for elem in array if elem < x]
        mid = [elem for elem in array if elem == x]
        more = [elem for elem in array if elem > x]
        array = glue(low, mid, more)
    return array


def glue(array1, array2, array3: list)->list:
    array = []
    for i in array1:
        array.append(i)
    for i in array2:
        array.append(i)
    for i in array3:
        array.append(i)
    return array
    