class Solution:
    def toLowerCase(self, s: str) -> str:
        strList = list(s)
        for i in range(0,len(s)) :
            if ord(strList[i]) >= 65 and ord(strList[i]) <= 90 :
                strList[i] = chr(ord(s[i]) + 32)
        return "".join(strList)

if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.toLowerCase("AZ")))
    print("result : {}".format(solution.toLowerCase("az")))