def quickSort(arr):
	quickSortHelp(arr,0,len(arr)-1)

def quickSortHelp(arr,first,last):
	if first < last:
		split = partition(arr,first,last)
		quickSortHelp(arr,first,split-1)
		quickSortHelp(arr,split+1,last)

def partition(arr,first,last):
	pivot = arr[first]
	left = first+1
	right = last
	dev = False

	while not dev:
		while left <= right and arr[left] <= pivot:
			left = left +1

		while left <= right and arr[right] >= pivot:
			right = right -1

		if left > right:
			dev = True

		else:
			temp = arr[left]
			arr[left]=arr[right]
			arr[right]=temp

	temp = arr[first]
	arr[first]=arr[right]
	arr[right]=temp

	return right


#arr = [54,26,93,17,77,31,44,55,20]
arr = [100,99,98,97,9000,898,2,3,1]
quickSort(arr)
print(arr)

