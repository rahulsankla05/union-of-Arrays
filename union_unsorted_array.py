# union_unsorted_array.py

def finalarray(arr1,arr2):
    arr =[]
# union = 1,2,3,4,5,6,7,8,9,10,11,18
    i=0 # index variable for arr1
    j=0 # indexing variable for arr2
    len1=len(arr1)
    len2 = len(arr2)
    while (i<len1):
        arr.append(arr1[i])
        i=i+1

    while(j<len2):
        arr.append(arr2[j])
        j=j+1
    return arr    

arr1= [1,2,7,3,8,10,9]
arr2 = [4,6,2,11,8,5,18]
arr = finalarray(arr1,arr2)
f= set(arr) #union of arr1 and arr2 will be print in set f
print(f)
