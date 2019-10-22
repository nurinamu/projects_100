import sys

class Solution:
    def isPalindrome(self, x: int) -> bool:
        print("value : {}".format(x))
        xStr = str(x)
        idx = 0
        while (idx < len(xStr) / 2) and (xStr[idx] == xStr[len(xStr)-1-idx]) :
            idx += 1
        return len(xStr) / 2 <= idx

if __name__ == "__main__":
    solution = Solution()
    print("result : {}".format(solution.isPalindrome(int(sys.argv[1]))))