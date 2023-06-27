def bubble(array: list)->list:
    for run in range(len(array)-1):
        for i in range(1,len(array)-run):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
    return array