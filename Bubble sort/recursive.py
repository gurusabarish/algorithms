# Create a list 
# Build recursive function
# Pass your list into function

def bubble_sort(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      arr[i],arr[i+1] = arr[i+1],arr[i]
      bubble_sort(arr)

lst = [64, 34, 25, 12, 22, 90, 11]
bubble_sort(lst)

print("Sorted array:");
for i in range(len(lst)):
	print(lst[i], end=' ')
