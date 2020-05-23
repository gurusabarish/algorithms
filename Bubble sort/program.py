# take an bytearray
# build an algorithms to sort
# pass your array into function
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

lst = [20,10,30,40,100,60,80,70,50,90]
bubblesort(lst)
print("Sorted list:",lst)
