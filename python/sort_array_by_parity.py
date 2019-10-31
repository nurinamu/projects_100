from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for num in A :
            if num % 2 == 0 :
                even.append(num)
            else :
                odd.append(num)
        even.extend(odd)
        return even

if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.sortArrayByParity([1,2,3,4,5,7,9,8,10])))