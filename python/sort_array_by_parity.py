from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) == 0 :
            return []
        rightIdx = len(A) - 1
        leftIdx = 0
        while leftIdx < rightIdx :
            while leftIdx < len(A) :
                if A[leftIdx] % 2 == 1 :
                    break
                else :             
                    leftIdx += 1
            while rightIdx >= 0 :
                if A[rightIdx] %2 == 0 :
                    break
                else :
                    rightIdx -= 1
            if leftIdx < rightIdx :        
                tmp = A[leftIdx]
                A[leftIdx] = A[rightIdx]
                A[rightIdx] = tmp
                leftIdx += 1
                rightIdx -= 1
        return A

if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.sortArrayByParity([1,2,3,4,5,7,9,8,10])))