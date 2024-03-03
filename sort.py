def ascending_order(arr):
    for i in range(len(arr)):
        index_min = i # VAR para armazenar o menor número da lista
        for j in  range(i+1,len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]


def descending_order(arr):
    for i in range(len(arr)):
        index_max = i # VAR para armazenar o menor número da lista
        for j in  range(i+1,len(arr)):
            if arr[j] > arr[index_max]:
                index_max = j
        arr[i], arr[index_max] = arr[index_max], arr[i]
    
