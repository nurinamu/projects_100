from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        inc = 0
        dec = len(S)
        result = []

        for flag in S:
            if flag == "I" :
                result.append(inc)
                inc += 1
            elif flag == "D" :
                result.append(dec)
                dec -= 1
        result.append(inc)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.diStringMatch("IDID"))
    print(s.diStringMatch("III"))
    print(s.diStringMatch("DDI"))
