def heapify(array, heap_size, root):  
    l = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and array[left] > array[l]:
        l = left
    if right < heap_size and array[right] > array[l]:
        l = right
    if l != root:
        array[root], array[l] = array[l], array[root]
        heapify(array, heap_size, l)

def heap(array):  
    size = len(array)
    for i in range(size, -1, -1):
        heapify(array, size, i)
    for i in range(size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)