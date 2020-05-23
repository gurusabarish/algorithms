# create a list 
# build obtimized algorithm
# pass your array in algorithm
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        swap=True
        for j in range(n-1-i):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = False
        if swap==False:
            break

lst = [20,10,30,40,100,60,80,70,50,90]
bubblesort(lst)
print("Sorted list:",lst)
