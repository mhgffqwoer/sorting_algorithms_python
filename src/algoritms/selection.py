def selection(array):  
    for i in range(len(array)):
        index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array