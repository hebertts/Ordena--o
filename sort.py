from time import time
def ascending_order(arr):
    start = time()
    for i in range(len(arr)):
        index_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]
    end = time()
    elapsed_time = end - start
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    miliseconds = float((end - start) * 1000)
    microssegundos = float((end - start) * 1_000_000)
    print(f'Tempo total: {minutes} minutos, {seconds} segundos, {format(miliseconds,"0.3f")} milissegundos, {format(microssegundos,"0.3f")} microssegundos')


def descending_order(arr):
    start = time()
    for i in range(len(arr)):
    
        index_max = i # VAR para armazenar o menor número da lista
        for j in  range(i+1,len(arr)):
            if arr[j] > arr[index_max]:
                index_max = j
        arr[i], arr[index_max] = arr[index_max], arr[i]
    end = time()
    elapsed_time = end - start
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    miliseconds = float((end - start) * 1000)
    microssegundos = float((end - start) * 1_000_000)
    print(f'Tempo total: {minutes} minutos, {seconds} segundos, {format(miliseconds,"0.3f")} milissegundos, {format(microssegundos,"0.3f")} microssegundos')

