from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evenIdx = []
        oddIdx = []

        for idx in range(0, len(A)) :
            if idx%2 == 0 :
                if A[idx]%2 != 0 :
                    if len(evenIdx) > 0 :
                        tmp = A[evenIdx[0]]
                        A[evenIdx[0]] = A[idx]
                        A[idx] = tmp
                        evenIdx = evenIdx[1:]
                    else :
                        oddIdx.append(idx)
            else :
                if A[idx]%2 == 0 :
                    if len(oddIdx) > 0 :
                        tmp = A[oddIdx[0]]
                        A[oddIdx[0]] = A[idx]
                        A[idx] = tmp
                        oddIdx = oddIdx[1:]
                    else :
                        evenIdx.append(idx)

        return A


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArrayByParityII([648,831,560,986,192,424,997,829,897,843]))