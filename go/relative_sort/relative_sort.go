package main

func getVal(idxMap map[int]int, idx int) int {
	if _, num := idxMap[idx]; num {
		return idxMap[idx]
	} else {
		return len(idxMap) + idx
	}
}

func qsort(arr []int, left int, right int, idxMap map[int]int) {
	if left >= right {
		return
	}

	var pivot = left
	var last = right
	var pivotVal = getVal(idxMap, arr[pivot])

	right++
	for left < right {
		for {
			left++
			if left >= right || getVal(idxMap, arr[left]) > pivotVal {
				break
			}
		}

		for {
			right--
			if right <= pivot || getVal(idxMap, arr[right]) < pivotVal {
				break
			}
		}
		if left < right {
			swap(arr, left, right)
		}
	}

	swap(arr, pivot, right)

	qsort(arr, pivot, right-1, idxMap)
	qsort(arr, right+1, last, idxMap)

	return
}

func swap(arr []int, x int, y int) {
	var tmp = arr[x]
	arr[x] = arr[y]
	arr[y] = tmp
}

func relativeSortArray(arr1 []int, arr2 []int) []int {

	var idxMap = make(map[int]int)

	for idx, num := range arr2 {
		idxMap[num] = idx
	}

	qsort(arr1, 0, len(arr1)-1, idxMap)

	return arr1
}

func main() {
	for _, val := range relativeSortArray([]int{2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19}, []int{2, 1, 4, 3, 9, 6}) {
		print(",", val)
	}
}
