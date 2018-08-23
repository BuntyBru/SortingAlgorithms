def selectionSort(arr):
	maximum = 0
	maximumIndex = -1
	lenArr = len(arr)-1
	while lenArr != 0:
		print(lenArr)
		for i in range(0,lenArr+1):
			if arr[i] > maximum:
				maximum = arr[i]
				maximumIndex = i
			
		arr[maximumIndex] = arr[lenArr]
		arr[lenArr] = maximum
		print(arr)
		print(maximum)
		print("--------------")
		maximum =0
		maximumIndex=-1
		lenArr = lenArr-1


arr = [54,118,26,93,17,77,31,44,55,20]
arr2 = [26,54,93,17,77,31,44,55,20]
arr3 = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20] 
selectionSort(arr3)
print(arr3)
