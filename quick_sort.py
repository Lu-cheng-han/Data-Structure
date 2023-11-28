


data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def partition(arr: list, low, high):
    base = arr[low]
    while (low < high):
        while (low < high and arr[high] >= base):
            high = high -1
        arr[low] = arr[high]
        while (low < high and arr[low] <= base):
            low = low + 1
        arr[high] = arr[low]
    arr[low] = base
    return low




def quick_sort(arr: list, low, high):
    if low < high:
        base = partition(arr, low, high)
        quick_sort(arr,low,base - 1)
        quick_sort(arr,base + 1,high)

if __name__ == "__main__":
    quick_sort(data, 0, len(data) - 1)
    print(data)
