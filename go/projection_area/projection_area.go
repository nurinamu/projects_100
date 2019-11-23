package main

func sum(arr []int) int {
	var sum = 0
	for _, num := range arr {
		sum += num
	}
	return sum
}

func projectionArea(grid [][]int) int {
	var cnt = 0
	maxX := make([]int, len(grid))
	maxY := make([]int, len(grid))

	for y, yArr := range grid {
		for x, height := range yArr {
			if len(maxX)-1 < y || maxX[y] < height {
				maxX[y] = height
			}
			if len(maxY)-1 < x || maxY[x] < height {
				maxY[x] = height
			}
			if height > 0 {
				cnt++
			}
		}
	}

	return cnt + sum(maxX) + sum(maxY)
}

func main() {
	print(projectionArea([][]int{{1, 2}, {3, 4}}))
}
