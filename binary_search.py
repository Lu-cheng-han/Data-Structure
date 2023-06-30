

def BinarySearch(arr,low,high,target):
    low = 0
    high = len(arr) - 1
   

    while low <= high:
        mid = (low+high)//2
        if arr[mid] ==target:
            return mid
        elif arr[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

a = [10,11,21,32,53,85,138,223,365]
print(BinarySearch(a,0,len(a)-1,70))
