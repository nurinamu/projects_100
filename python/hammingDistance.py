class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = "{}".format(format(x ^ y, "b"))
        distance = 0
        start = 0
        print(xor)
        for ch in xor :
            if ch == "1" :
                if start == 1 :
                    start = 2
                    break
                else :
                    start = 1
            if start == 1 :
                distance += 1
        return distance if start == 2 else 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingDistance(14, 3))