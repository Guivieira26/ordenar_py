def mergesort(array,esq,dir):
    """
    Merge sort recursivo que divide o array em dois subarrays e os ordena
    """
    if esq >= dir:
        return
    
    
    meio = (esq + dir) //2
    mergesort(array, esq, meio)
    mergesort(array, meio + 1, dir)
    merge(array, esq, meio, dir)

"""
comparar os dois subarrays e colocar o menor deles na posição correta
"""
def merge(array, esq, meio, dir):
    #criar copia subarray
    copy_esq = array[esq:meio +1] #cria o subarray da esquerda
    copy_dir = array[meio+1:dir+1] #cria o subarray da direita
    print ("array esquerda: ",copy_esq)
    print ("array direita: ",copy_dir)
    i = j = 0
    k = esq
    while i <len(copy_esq) and j<len(copy_dir):
        if(copy_esq[i]<=copy_dir[j]): #compara os dois subarrays ou seja, se o da esquerda é menor que o da direita substitui o valor 
            array[k] = copy_esq[i]
            i+=1
        else:
            array[k] = copy_dir[j]
            j+=1
        k+=1
    while i< len(copy_esq):
        array[k] = copy_esq[i]
        i+=1
        k+=1
    while j< len(copy_dir):
        array[k] = copy_dir[j]
        j+=1
        k+=1
