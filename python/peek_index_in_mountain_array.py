from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = -1
        for idx in range(0, len(A)) :
            if peak < A[idx] :
                peak = A[idx]
            else :
                return idx - 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.peakIndexInMountainArray([0,1,0]))