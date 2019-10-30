from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for inside in A :
            lenInside = len(inside)
            for idx in range(0, int(lenInside / 2)) :
                tmp = inside[idx]
                lastIdx = lenInside - 1 - idx
                inside[idx] = 1 - inside[lastIdx]
                inside[lastIdx] = 1 - tmp
            if lenInside % 2 == 1 :
                inside[int(lenInside / 2)] = 1 - inside[int(lenInside / 2)]
        return A

if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.flipAndInvertImage([[1,0,1],[0,1,0],[1,1,0]])))