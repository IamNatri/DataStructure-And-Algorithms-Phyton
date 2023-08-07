import timeit
import random
import numpy as np
import sys

sys.path.append('C:\\Users\\matheusb\\Documents\\Cursos\\EstruturaDeDados-Phyton\\Algoritmos')


from DataStructure.VetorOrdenado import vetorOrdenado
from BubbleSort import bubble_sort
from InsertionSort import insertionSort
from QuickSort import quickSort
from SelectionSort import selection_sort
from ShellSort import shellSort

arr = np.array([random.random() for _ in range(5000)])

vec = vetorOrdenado(len(arr))

def insereelements():
   for i in range(0, len(arr) - 1):
        vec.insere(arr[i])

execution_time_vetorordenado = timeit.timeit(lambda: insereelements(), number=1)
print("Tempo de execução vetorOrdenado:", execution_time_vetorordenado, "segundos")


execution_time_bubble_sort = timeit.timeit(lambda: bubble_sort(arr.copy()), number=1)
print("Tempo de execução bubble_sort:", execution_time_bubble_sort, "segundos")

execution_time_selectionsort = timeit.timeit(lambda: selection_sort(arr.copy()), number=1)
print("Tempo de execução selection_sort:", execution_time_selectionsort, "segundos")

execution_time_insertionSort = timeit.timeit(lambda: insertionSort(arr.copy()), number=1)
print("Tempo de execução insertionSort:", execution_time_insertionSort, "segundos")

execution_time_shellSort = timeit.timeit(lambda: shellSort(arr.copy()), number=1)
print("Tempo de execução shellSort:", execution_time_shellSort, "segundos")

execution_time_quickSort = timeit.timeit(lambda: quickSort(arr.copy(), 0, len(arr) -1 ), number=1)
print("Tempo de execução quickSort:", execution_time_quickSort, "segundos")