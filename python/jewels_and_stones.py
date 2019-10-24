import re

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        dic = {}
        for ch in J :
            dic[ch] = 1
        for ch in S :
            if ch in dic :
                cnt += 1
        return cnt

if __name__ == "__main__":
    solution = Solution()
    print(solution.numJewelsInStones("aA","aasdfasdAAAaa"))