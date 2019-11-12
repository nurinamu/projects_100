from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        chLen = len(A[0])
        wordsLen = len(A)
        fail = 0
        for chIdx in range(0, chLen) :
            prev = 0
            for wordIdx in range(0, wordsLen) :
                ordVal = ord(A[wordIdx][chIdx])
                if ordVal - prev >= 0 :
                    prev = ordVal  
                else :
                    fail += 1
                    break

        return fail

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDeletionSize(["cba","daf","ghi"]))
    print(sol.minDeletionSize(["a","b"]))
    print(sol.minDeletionSize(["zyx","wvu","tsr"]))