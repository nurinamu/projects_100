class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rCnt = 0
        lCnt = 0
        totalCnt = 0
        for ch in s :
            if ch == 'R' :
                rCnt += 1
            if ch == 'L' :
                lCnt += 1

            if lCnt == rCnt :
                totalCnt += 1
                lCnt = 0
                rCnt = 0
            
        return totalCnt

if __name__ == "__main__":
    solution = Solution()
    print("result 3 : {}".format(solution.balancedStringSplit("RLLLLRRRLR")))
    print("result 4 : {}".format(solution.balancedStringSplit("RLRRLLRLRL")))
