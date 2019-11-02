from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = {}
        for num in A :
            if num in dic :
                dic[num] += 1
            else :
                dic[num] = 1

        times = len(A) / 2
        for key in dic :
            if dic[key] == times :
                return key                

        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.repeatedNTimes([1,2,3,4,4,4]))