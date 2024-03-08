from time import time

file_path = "resultados.txt"  # Caminho do arquivo onde os resultados serão armazenados

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
    milliseconds = float((end - start) * 1000)
    microseconds = float((end - start) * 1_000_000)
    print(f'Tempo total: {minutes} minutos, {seconds} segundos, {format(milliseconds,"0.3f")} milissegundos, {format(microseconds,"0.3f")} microssegundos')
    with open(file_path, "a") as file:
        file.write(f'Tempo total: {minutes} minutos, {seconds} segundos, {format(milliseconds,"0.3f")} milissegundos, {format(microseconds,"0.3f")} microssegundos\n')
        if isinstance(arr[i],str):
            file.write(f'Array ordenado possui {len(arr)} nomes\n')
        else:
            file.write(f'Array ordenado 1 a {max(arr)}\n')
        file.close()

def descending_order(arr):
    start = time()
    for i in range(len(arr)):
    
        index_max = i # VAR para armazenar o menor número da lista
        for j in  range(i+1,len(arr)):
            if arr[j] > arr[index_max]:
                index_max = j
        arr[i], arr[index_max] = arr[index_max], arr[i]
    '''arr = sorted(arr, reverse=True)'''
    end = time()
    elapsed_time = end - start
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = float((end - start) * 1000)
    microseconds = float((end - start) * 1_000_000)
    print(f'Tempo total: {minutes} minutos, {seconds} segundos, {format(milliseconds,"0.3f")} milissegundos, {format(microseconds,"0.3f")} microssegundos')

    with open(file_path, "a") as file:
            file.write(f'Tempo total: {minutes} minutos, {seconds} segundos, {format(milliseconds,"0.3f")} milissegundos, {format(microseconds,"0.3f")} microssegundos\n')
            if isinstance(arr[i],str):
                file.write(f'Array ordenado possui {len(arr)} nomes\n')
            else:
                file.write(f'Array ordenado 1 a {len(arr)}\n')
                file.close()