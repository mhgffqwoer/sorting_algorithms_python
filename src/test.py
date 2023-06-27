from random import randint, shuffle


def merge(array):
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        merge(lefthalf)
        merge(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
    return array

def direct(length: int)->list:
    array = []
    for i in range(length):
        array.append(i)
    return array

def random(length: int)->list:
    array = direct(length)
    shuffle(array)
    return array

array = random(30)
print(array)
