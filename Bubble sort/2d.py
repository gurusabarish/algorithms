# Create a list
# build your algorithm
# Pass your list into function

def bubblesort(arr):
    n = len(lst)
    for i in range(n):
        m = len(arr[i])

        for j in range(m):
            for k in range(m-j-1):
                if lst[i][k]>lst[i][k+1]:
                    lst[i][k], lst[i][k+1] = lst[i][k+1], lst[i][k]
    
lst = [[10,6,9,7,8],[4,2,5,3,1],[3,6,4,7,5]]
bubblesort(lst)
print("Sorted list: ")
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end=" ")
    print()
