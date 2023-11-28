import random
data = [random.randint(0, 100) for _ in range(20)]



def BubbleSort(arr: list):
    length = len(arr)
    for j in range(length - 1):
        for i in range(length - j - 1):
            if arr[i] < arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

print(data)
BubbleSort(data)
print(data)