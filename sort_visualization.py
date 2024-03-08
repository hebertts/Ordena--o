import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

def selection_sort(data):
    start_time = time.time() # Inicia a contagem do tempo para a ordenação
    n = len(data) # Obtém o tamanho da lista de dados
    for i in range(n):
        min_index = i # Define o índice atual como o índice do valor mínimo
        for j in range(i+1, n): # Itera sobre os elementos restantes da lista
            if data[j] < data[min_index]: # Verifica se o elemento atual é menor que o mínimo atual
                min_index = j # Atualiza o índice do valor mínimo
            yield data, i, j, min_index, time.time() - start_time # Retorna o estado atual da ordenação

        # Troca os elementos nas posições i e min_index
        data[i], data[min_index] = data[min_index], data[i]
        # Retorna o estado atual da ordenação após a troca
        yield data, i, j, min_index, time.time() - start_time

# Função para atualizar o gráfico de barras durante a animação
def update_chart(frame, bars, patches, timer_text):
    # Extrai os dados do frame atual
    data, i, j, min_index, elapsed_time = frame
    
    # Atualiza a altura de cada barra de acordo com os dados atualizados
    for k, bar in enumerate(bars):
        bar.set_height(data[k])
        # Define a cor das barras dependendo da sua posição na ordenação
        if k <= i:
            patches[k].set_facecolor('lightgreen')  # Barras já ordenadas ficam em verde claro
        else:
            patches[k].set_facecolor('lightblue')   # Barras ainda não ordenadas ficam em azul claro

    # Destaca a barra atualmente sendo comparada com as outras
    patches[j].set_facecolor('red')   # Barra sendo comparada fica em vermelho
    # Destaca a barra com o valor mínimo encontrado durante a busca
    patches[min_index].set_facecolor('yellow')  # Barra com valor mínimo fica em amarelo

    # Atualiza o texto do timer com o tempo decorrido até o momento
    timer_text.set_text(f"Tempo Decorrido: {elapsed_time:.2f} segundos\n")


# Função para a visualização do selection sort
def selection_sort_visualization(data):
    # Cria uma figura e eixos para o gráfico
    fig, ax = plt.subplots()
    
    # Obtém o comprimento dos dados
    n = len(data)
    
    # Cria uma matriz de posições x para as barras
    x = np.arange(n)
    
    # Cria as barras para o gráfico
    bars = ax.bar(x, data, align='edge')
    
    # Cria os patches para as barras
    patches = [rect for rect in bars]
    
    # Define os limites dos eixos x e y
    ax.set_xlim(0, n)
    ax.set_ylim(0, max(data) + 5)
    
    # Define o título do gráfico
    ax.set_title("Visualização do Selection Sort")

    # Adiciona um texto para exibir o tempo decorrido
    timer_text = ax.text(0.5, 1.05, "", transform=ax.transAxes, ha='center')
    
    # Cria a animação usando a função FuncAnimation do matplotlib
    ani = animation.FuncAnimation(fig, update_chart, frames=selection_sort(data), fargs=(bars, patches, timer_text), interval=50, repeat=False)
    
    # Exibe o gráfico animado
    plt.show()

# Verifica se este script está sendo executado como o programa principal
if __name__ == "__main__":
    # Gera uma lista de números aleatórios para ordenar
    data = np.random.randint(10,300,size=30)

    # Chama a função de visualização do selection sort
    selection_sort_visualization(data)
