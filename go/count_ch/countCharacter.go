package main

func countCharacters(words []string, chars string) int {
	var charMap map[string][]int
	charMap = make(map[string][]int)
	for idx, ch := range chars {
		charMap[string(ch)] = append(charMap[string(ch)], idx)
	}

	var cnt int
	cnt = 0
	var resultMap map[int]int
	for _, word := range words {
		resultMap = make(map[int]int)
		for _, ch := range word {
			if value, found := charMap[string(ch)]; found {
				for _, idx := range value {
					if val, fnd := resultMap[idx]; fnd {
						continue
					} else {
						resultMap[idx] = val
						break
					}
				}
			}
		}
		if len(resultMap) == len(word) {
			cnt += len(word)
		}
	}
	return cnt
}

func main() {
	println(countCharacters([]string{"cat", "bt", "hat", "tree"}, "atach"))
	println(countCharacters([]string{"hello", "world", "leetcode"}, "welldonehoneyr"))
}
