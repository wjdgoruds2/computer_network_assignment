import sys

def quick_sort(arr):
	if len(arr)>1:
		pivot = arr[len(arr)-1]
		left, mid, right = [],[],[]
		for i in range(len(arr)-1):
			if arr[i]<pivot:
				left.append(arr[i])
			elif arr[i]>pivot:
				right.append(arr[i])
			else:
				mid.append(arr[i])
		mid.append(pivot)
		return quick_sort(left)+mid+quick_sort(right)
	else:
		return arr

arr = []
result = []
for n in range(len(sys.argv)-sys.argv.index("-o")-3):
	arr.append(int(sys.argv[sys.argv.index("-o")+n+3]))

if sys.argv[(sys.argv.index("-o"))+1]=="A":
	result = quick_sort(arr)
elif sys.argv[(sys.argv.index("-o"))+1]=="D":
	result = quick_sort(arr)
	result.reverse()
print(result)


