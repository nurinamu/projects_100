class Solution:
    def toLowerCase(self, s: str) -> str:
        retStr = ''
        for i in range(0,len(s)) :
            if ord(s[i]) >= 65 and ord(s[i]) <= 90 :
                retStr += chr(ord(s[i]) + 32)
            else :
                retStr += s[i]
        return retStr

if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.toLowerCase("AZ")))
    print("result : {}".format(solution.toLowerCase("az")))