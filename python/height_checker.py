from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted = heights.copy()
        sorted.sort()

        cnt = 0

        for idx in range(0, len(sorted)) :
            if sorted[idx] != heights[idx] :
                cnt += 1

        return cnt

if __name__ == "__main__":
    sol = Solution()
    print(sol.heightChecker([1,1,4,2,1,3]))
