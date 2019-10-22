class Solution:
    numStr = "MDCLXVI"
    numStrVal = [1000, 500, 100, 50, 10, 5, 1]
    def romanToInt(self, s: str) -> int:        
        sum = 0
        prevVal = 0
        for i in range(len(s)-1 , -1, -1) :
            curVal = Solution.numStrVal[Solution.numStr.index(s[i])]
            if prevVal <= curVal :
                sum += curVal
            else :
                sum -= curVal
            prevVal = curVal
        return sum


if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.romanToInt('III')))
    print("result : {}".format(solution.romanToInt('IV')))
    print("result : {}".format(solution.romanToInt('IX')))
    print("result : {}".format(solution.romanToInt('MCMXCIV')))