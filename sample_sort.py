import time
import random

data = [random.randint(0, 100) for _ in range(100000)]


def SampleSort(arr: list):

    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
start_time = time.time()
SampleSort(data)
end_time = time.time()
print('total time',end_time - start_time)
        