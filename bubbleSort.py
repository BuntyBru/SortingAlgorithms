def bubbleSort(arr):
	lenArr = len(arr)-1;
	while lenArr > 0:

		for i in range(lenArr):
			if arr[i] > arr[i+1]:
				temp = arr[i]
				arr[i]= arr[i+1]
				arr[i+1] = temp
		lenArr = lenArr-1

arr = [54,26,93,17,77,31,44,55,20]
arr2 = [100,90,80,2,1]
bubbleSort(arr)
bubbleSort(arr2)

print(arr)
print(arr2)