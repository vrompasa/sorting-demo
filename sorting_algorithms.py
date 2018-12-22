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

        return self._merge(left, right)

    def _merge(self, left, right):
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
