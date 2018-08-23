def insertionSort(arr):
	for i in range(1,len(arr)):
		curr = arr[i]
		pos = i 

		while pos > 0 and arr[pos-1] > curr:
			arr[pos]= arr[pos-1]
			pos = pos-1
		arr[pos] = curr

arr =  [54,26,93,17,77,31,44,55,20]
insertionSort(arr)
print(arr)
