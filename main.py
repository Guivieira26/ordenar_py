import merge
import quick
import random
import time
inicio = time.time()
# This is a test file
#"""
x = [111,100002231,10,6,8,4,2,1,3,5,7,9,17,29,4,68,43,23,13,102,768] # teste 1 a 10
#teste array menor
print(x)
#merge.mergesort(x,0,len(x)-1) #ordena em mergesort
quick.quick(x,esq=0,dir=len(x)-1) #ordena em quicksort
print(x)
#"""

"""
array_colossal = [random.randint(1, 999999999999999999999999999999999999999999999999999) for _ in range(500000)] # de 1 a 10^50 para 5000 elementos
print(array_colossal)
merge.mergesort(array_colossal,0,len(array_colossal)-1)
print(array_colossal)
fim = time.time()
print("O tempo de execução foi de: ", fim - inicio)
"""