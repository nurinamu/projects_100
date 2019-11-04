from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1) :
            numStr = str(num)
            cnt = 0
            for numCh in numStr :
                if numCh != "0" and num % int(numCh) == 0 :
                    cnt += 1
                else :
                    break
                    
            if cnt == len(numStr) :
                result.append(num)
        
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.selfDividingNumbers(1,100))