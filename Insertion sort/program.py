# Create a list 
# Build insertionsort algorithm
# Pass your list into function

def insertionsort(arr):
  for i in range(1, len(arr)):
    j=i-1
    while j>=0 and arr[i]<arr[j]:
      arr[i],arr[j] = arr[j],arr[i]

lst = [20,10,30,40,100,60,80,70,50,90]
insertionsort(lst)

print("Sorted list:");
for i in range(len(lst)):
	print(lst[i], end=' ')
