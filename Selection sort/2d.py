# Create a list
# Build algorithm
# pass your list into function

def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        m = len(arr[i])
        for j in range(m):
            min_idx = j
            for k in range(j+1,m):
                if arr[i][min_idx]>arr[i][k]:
                    min_idx = k
            arr[i][min_idx], arr[i][j] = arr[i][j], arr[i][min_idx]
            
lst = [[10,6,9,7,8],[4,2,5,3,1],[3,6,4,7,5]]
selectionsort(lst)
print("Sorted list:")
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end=" ")
    print()
