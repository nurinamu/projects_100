from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for idx in range(0, len(nums) - 1, 2) :
            sum += nums[idx]
        return sum

if __name__ == "__main__":
    solution = Solution()
    print(solution.arrayPairSum([1,2,3,4]))
    print(solution.arrayPairSum([1,1]))