

def swap(array:list,i:int,min_index:int):
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp



arr1 = [0,4,8,-5,6,10,-3]

for i in range(len(arr1)):
    min_index = i
    for j in range(i+1,len(arr1)):
        if arr1[min_index] > arr1[j]:
            min_index = j 
    swap(arr1,i,min_index)

print(arr1)
    
    



