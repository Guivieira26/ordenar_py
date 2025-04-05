def quick(array,esq, dir):
    if esq < dir:
        pivo = partition(array,esq,dir)
        quick(array, esq, pivo - 1)
        quick(array, pivo + 1, dir)
    
def partition(array,esq,dir):
    pivo = array[dir] #escolhe o último elemento como pivo (padrao do lomuto)
    i = esq -1 

    for j in range(esq , dir):
        if (array[j] < pivo):
            i+= 1
            array[i], array [j] = array[j], array[i] #troca os valores de i e j, ou seja, o menor valor vai para a esquerda e o maior valor vai para a direita
    # troca o pivo com o valor que está na posição i, ou seja, o menor valor vai para a esquerda e o maior valor vai para a direita        
    array[i+1], array[dir] = array[dir], array[i+1]
    return i +1