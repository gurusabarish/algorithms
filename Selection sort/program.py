# Create a list
# build your algorithm
# Pass your list into function

def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_term = i
        for j in range(i+1,n):
            if arr[min_term]>arr[j]:
                min_term = j
        arr[min_term], arr[i] = arr[i], arr[min_term]
        
lst = [20,10,30,40,100,60,80,70,50,90]
selectionsort(lst)
print("Sorted list: ",lst)
