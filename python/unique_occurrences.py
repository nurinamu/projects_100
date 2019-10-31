from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for num in arr :
            if num in map :
                map[num] += 1
            else :
                map[num] = 1
        dist = {}
        for key in map :
            print(key)
            if map[key] in dist :
                return False
            else :
                dist[map[key]] = 1

        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniqueOccurrences([1,1,1,2,2,3]))