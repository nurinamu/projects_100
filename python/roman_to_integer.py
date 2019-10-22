class Solution:
    dic = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    def romanToInt(self, s: str) -> int:        
        sum = 0
        prevVal = 0
        for i in range(len(s) - 1 , -1, -1) :
            curVal = Solution.dic[s[i]]
            if prevVal <= curVal :
                sum += curVal
            else :
                sum -= curVal
            prevVal = curVal
        return sum


if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.romanToInt('LVIII')))
    print("result : {}".format(solution.romanToInt('IV')))
    print("result : {}".format(solution.romanToInt('IX')))
    print("result : {}".format(solution.romanToInt('MCMXCIV')))