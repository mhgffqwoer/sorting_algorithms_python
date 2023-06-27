def insertion(array):  
    for i in range(1, len(array)):
        item = array[i]
        i2 = i - 1
        while i2 >= 0 and array[i2] > item:
            array[i2 + 1] = array[i2]
            i2 -= 1
        array[i2 + 1] = item
    return array