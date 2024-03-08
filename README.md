# Sort Visualization ![alt text](image-5.png)
Documentação referente a aplicação *sort_visualizatiton.py*. Com o intuito de mostrar como  algoritmo de ordenação Selection Sort funciona e como ele faz para ordenar os dados de forma cresente ou decrescente, utilizando a biblioteca matplotlib para mostrar visualmente como o algoritmo seleciona os dados. 

# Importações ![alt text](image-4.png)
| Library | Description |
| --- | --- |
| `matplotlib` | Criar gráficos e visualizações *estáticas, interativas e animadas* |
| `numpy` | Fornece suporte para **arrays** multidimensionais e funções matemáticas |
| `time` | Fornece funções para acessar e manipular informações sobre o tempo |

Para utilizar o matplotlib é necessário fazer o **pip install matplotlib**

# Código  ![alt text](image-6.png)

**Main:**

Para verificar se o script está sendo executado diretamente como o programa principal ou se está sendo importado como um módulo em outro script.

     if __name__ == "__main__": 

Na array *data* está armazenando números de no intervalo de números desejados, isso é graças ao submódulo `random`do `Numpy`. A função `randint` gera números inteiros aletórios dentro de um intevalo espécificado e com o tamanho de n elementos na array. 

    data = np.random.randint(número inicial,limite superior,size=quantidade de elementos desejado)

**selection_sort_visualization:**

Criação da figura e eixos do gráfico, *fig* aqui é a área onde os gráficos são desenhados. *ax* será nossos eixos, espaços onde os dados são plotados, podendo pensar neles como contêineres para os gráficos propriamente ditos.

    fig, ax = plt.subplots()

Criação de uma matriz de posições x para as barras com o mesmo comprimento dos dados, assim representado o eixo x do nosso gráfico, facilitando a distribuição dos dados ao longo do eixo.

    x = np.arange(n)

Criação de barras usando as posiçoes especificadas, o tamanho dessas barras será de acordo com a array, são os dados que vamos querer visualizar, `ax.bar` método usado para criar as barras em gráfico

    bars = ax.bar(posições da barra, altura das barras, alinhamento a esqueda(align='edge'))
   
Essa linha é necessária para atualizar nossas barras posteriormente conforme necessário.
    
    patches = [rect for rect in bars]
* [rect for rect in bars]: Esta é uma compreensão de lista em Python que itera sobre a lista de barras (bars) e cria uma nova lista contendo as referências para cada objeto retangular que representa uma barra no gráfico.

* for rect in bars: Itera sobre cada barra na lista bars.
* rect: É a variável que representa cada objeto retangular (ou barra) na lista bars.
* rect for rect in bars: Retorna a referência para cada objeto retangular na lista bars.


Adiciona um texto para exibir o tempo decorrido

    timer_text = ax.text(largura, altura, texto desejado, coordenadas para posicionar o texto, ha=alinhamento do texto)

Cria a animação usando a função FuncAnimation do matplotlib

    animation.FuncAnimation(fig, func, frames, fargs, interval, repeat_delay, blit)
* fig: A figura onde a animação será desenhada.
* func: A função de atualização que será chamada em cada quadro da animação.
* frames: Este parâmetro especifica os quadros da animação.
* fargs: Uma tupla de argumentos extras para passar para a função de atualização func.
* interval: O intervalo de tempo entre cada quadro da animação, em milissegundos.
* repeat_delay: Um intervalo de tempo em milissegundos a ser aguardado após a conclusão da * reprodução de uma animação antes que a próxima seja iniciada. Este parâmetro só é usado se * * * repeat for True.
* blit: Um booleano que indica se deve ser usada a técnica de "blitting" para otimizar a animação.

**update_chart**

Essa função é essencial para atualizar os valores mostrado no gráfico e seus efeitos
1. Extração dos dados:

    * data, i, j, min_index, elapsed_time = *frame:* Extrai os dados do quadro atual da animação. *data* contém os valores das barras, *i* é o índice atual do loop externo de ordenação, *j* é o índice atual do loop interno de ordenação, *min_index* é o índice do valor mínimo encontrado durante a busca e *elapsed_time* é o tempo decorrido até o momento.

2. Atualizando os valores de acordo com os dados:

    * bar.set_height(data[k]): Define a altura de cada barra de acordo com os dados atualizados do quadro.
    * if k <= i:: Verifica se a barra está ordenada até o índice i e define a cor como verde claro se estiver. Caso contrário, define a cor como azul claro.
    * patches[j].set_facecolor('red'): Destaca a barra atualmente sendo comparada em vermelho.  
    * patches[min_index].set_facecolor('yellow'): Destaca a barra com o valor mínimo encontrado durante a busca em amarelo.
    * timer_text.set_text(f"Tempo Decorrido: {elapsed_time:.2f} segundos\n"): Atualiza o texto do timer com o tempo decorrido até o momento.

**selection_sort**

Essencialmente, essa função permite iterar sobre o processo de ordenação do "Selection Sort" passo a passo, fornecendo informações sobre o estado da ordenação e o tempo decorrido em cada etapa
    
    data = [10,20,30,50,64,1]
    start_time = time.time() 
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n): 
            if data[j] < data[min_index]: atual
                min_index = j 
            yield data, i, j, min_index, time.time() - start_time 
        data[i], data[min_index] = data[min_index], data[i]
        yield data, i, j, min_index, time.time() - start_time

1. Iniciando a contagem do *tempo: start_time = time.time()*. Isso inicia a contagem do tempo antes de iniciar a ordenação. Será usado para calcular o tempo decorrido durante a ordenação.

2. Obtendo o tamanho da lista de dados: *n = len(data)*. Isso obtém o tamanho da lista de dados passada como parâmetro para a função.

3. Loop externo para percorrer a lista: *for i in range(n):*. Este loop externo percorre a lista do início ao fim.

4. Inicializando o índice do valor mínimo: *min_index = i*. No início de cada iteração do loop externo, o índice do valor mínimo é definido como o índice atual i.

5. Loop interno para encontrar o valor mínimo: *for j in range(i+1, n):*. Este loop interno percorre os elementos restantes da lista a partir do próximo elemento após o índice i.

6. Comparando os elementos para encontrar o mínimo: *if data[j] < data[min_index]:*. Verifica se o elemento atual é menor que o mínimo atual. Se for, atualiza min_index com o índice do novo valor mínimo encontrado.

7. Retornando o estado atual da ordenação: *yield data, i, j, min_index, time.time() - start_time*. A cada iteração do loop interno, retorna o estado atual da ordenação, que inclui a lista de dados atualizada, os índices i, j, min_index e o tempo decorrido desde o início da ordenação.

8. Troca os elementos nas posições i e min_index: *data[i], data[min_index] = data[min_index], data[i]*. Após encontrar o valor mínimo, troca os elementos nas posições i e min_index para colocar o valor mínimo na posição correta.

9. Retornando o estado atual após a troca: *yield data, i, j, min_index, time.time() - start_time*. Retorna o estado atual da ordenação após a troca dos elementos.

Um dos motivos de utilizar o **yield** pelo fato de:

1. Iteração sob demanda:

    Com o yield, podemos iterar sobre os resultados produzidos pelo gerador um de cada vez. Isso é útil quando queremos processar ou visualizar os resultados incrementalmente, como em uma animação ou em um loop de processamento.
    Continuidade do estado da função:

2. O yield permite que a função mantenha seu estado interno entre as chamadas.

    Isso significa que, quando a função é chamada novamente, ela continua a partir do ponto em que foi interrompida, mantendo os valores das variáveis locais. No caso do algoritmo de ordenação, isso é útil para manter o estado do processo de ordenação entre as iterações do loop.
