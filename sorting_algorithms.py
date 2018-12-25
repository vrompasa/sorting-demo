import math
import statistics

class InsertionSort():
    def __init__(self):
        self.name = "insertion sort"

    def sort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

        return array

class MergeSort():
    def __init__(self):
        self.name = "merge sort"

    def sort(self, array):
        if len(array) == 1:
            return array

        middle = len(array) // 2
        left = self.sort(array[:middle])
        right = self.sort(array[middle:])

        return self.__merge(left, right)

    def __merge(self, left, right):
        array = []
        # Add infinities to aid comparison
        if left[-1] != math.inf and right[-1] != math.inf:
            left.append(math.inf)
            right.append(math.inf)
        i = 0
        j = 0
        for k in range(len(left) - 1 + len(right) - 1):
            if left[i] <= right[j]:
                array.append(left[i])
                if i < len(left) - 1:
                    i += 1
            else:
                array.append(right[j])
                if j < len(right) - 1:
                    j += 1
        return array

class QuickSort():
    def __init__(self):
        self.name = "quicksort"

    def sort(self, array):
        less = []
        pivotList = []
        more = []
        if len(array) == 0:
            return array
        else:
            pivot = statistics.median([array[0], array[len(array) // 2], array[-1]])
            for number in array:
                if number < pivot:
                    less.append(number)
                elif number > pivot:
                    more.append(number)
                else:
                    pivotList.append(number)
            less = self.sort(less)
            more = self.sort(more)
        return less + pivotList + more

class HeapSort():
    def __init__(self):
        self.name = "heapsort"

    def sort(self, array):
        heap_size = len(array)
        self.__build_heap(array, heap_size)
        for i in range(heap_size-1, 0, -1):
            array[0], array[i] = array[i], array[0]
            heap_size -= 1
            self.__max_heapify(array, heap_size, 0)

    def __build_heap(self, array, heap_size):
        for i in range((heap_size//2), -1, -1):
            self.__max_heapify(array, heap_size, i)

    def __max_heapify(self, array, heap_size, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < heap_size and array[left] > array[largest]:
            largest = left
        if right < heap_size and array[right] > array[largest]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.__max_heapify(array, heap_size, largest)
